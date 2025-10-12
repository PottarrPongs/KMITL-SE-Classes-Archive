from fastapi import FastAPI, Body, Request, HTTPException, Depends, Header
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from random import randint
import bcrypt

app = FastAPI()

@app.get("/")
async def root():
    return "Hello, World!"

def hash_password(password: str):
    password_utf8 = password.encode("utf-8")
    return bcrypt.hashpw(password_utf8, bcrypt.gensalt())

def verify_password(plain_password: str, hashed_password):
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password)

user_db = {
    "1": {
        "id": "1",
        "name": "Name ForExample",
        "enroll": []
    },
    "2": {
        "id": "2",
        "name": "Nixon",
        "enroll": []
    },
}

user_pw = {
    "1": {
        "hashed_password": hash_password("Name")
    },
    "2": {
        "hashed_password": hash_password("NixOS")
    },
}

user_token = dict()

@app.get("/student/all")
async def get_all_std():
    return user_db

@app.post("/login")
async def login(id: str = Body(), password: str = Body()):
    user_record = user_db.get(id)
    if not user_record:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    if not verify_password(password, user_pw[id]["hashed_password"]):
        raise HTTPException(status_code=400, detail="Invalid username or password")
    return {"message": "Login successful"}

@app.post("/student/new")
async def new_std(id: str = Body(), name: str = Body(), password: str = Body()):
    if id in user_db:
        raise HTTPException(status_code=400, detail="User already exists")
    else:
        new_user = {
            "id": id,
            "name": name,
            "enroll": []
        }
        
        user_db[id] = new_user
        user_pw[id] = {
        "hashed_password": hash_password(password)
        }
        print(user_db)
        return {
            "detail": "Created Successfully"
        } 

@app.post("/student/login")
async def login_std(id: str = Body(), password: str = Body()):
    if id not in user_db:
        return {
            "detail": "Invalid username or password"
        } 
    else:
        if verify_password(password, user_pw[id]["hashed_password"]):
            new_token = gen_token(id)
            print(new_token)

            return {
                "access_token": f"token {new_token}",
                "token_type": "token"
            }
        else:
            return {
                "detail": "Invalid username or password"
            } 


def gen_token(id:str):
    for token in user_token:
        if user_token[token] == id:
            return token
    token = "%020x" %(randint(0, 0xffffffffffffffffffff))
    while token in user_token:
        token = "%020x" %(randint(0, 0xffffffffffffffffffff))
    user_token[token] = id
    return token

@app.post("/student/enroll")
async def std_enroll(id: str = Body(), name: str = Body(), grade: str = Body(), auth: str = Header()):
    user_record = get_current_user(auth)

    print(user_record)


def verify_token(token: str):
    token = token.lower()
    if token in user_token:
        return user_token[token]
    return None

async def get_current_user(auth: str = Header(...)):
    if not auth.startswith("token "):
        raise HTTPException(status_code=401, detail="Invalid Token Auth")
    token = auth[len("token "):].strip()
    id = verify_token(token)
    if not id:
        raise HTTPException(status_code=401, detail="Invalid or Expired Token")
    user_record = user_db.get(id)
    print(user_record)
    if not user_record:
        raise HTTPException(status_code=401, detail="User not found")
    return user_record

