from typing import Annotated, Optional
from fastapi import FastAPI, Request
from pydantic import BaseModel
import bcrypt
import jwt
import datetime

app = FastAPI()
SECRET_KEY = "i_love_osu_very_much"  # store in env var in real projects

def hashPassword(p: str):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(p.encode("utf-8"), salt)
    return hashed

def create_access_token(user_id: str):
    id = "user" + user_id
    payload = {
        "sub": id,  # subject (user identifier)
        "iat": datetime.datetime.now(datetime.timezone.utc)  # issued at
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

class Student(BaseModel):
    id: str
    name: str
    password: str

class StudentLogin(BaseModel):
    id: str
    password: str

class Secret(BaseModel):
    secret: str 

students = {
    "1": {
        "id": "1",
        "name": "Alice",
        "secret": "I am a lesbian"
    },
    "2": {
        "id": "2",
        "name": "Bob",
        "secret": "I love men"
    }
}

studentsHash = {
    "1": {
        "access_token": create_access_token("1"),
        "token_type": "token"
    },
    "2": {
        "access_token": create_access_token("2"),
        "token_type": "token"
    }
}

studentsPassword = {
    "1": hashPassword("abc"),
    "2": hashPassword("def")
}

@app.get("/students/all")
def getAllStudents():
    return students

@app.post("/students/new")
def newStudent(stu: Student):
    if stu.id in students:
        return {"detail": "Student already exists"}
    else:
        students[stu.id] = {
            "id": stu.id,
            "name": stu.name,
            "secret": "None"
        }
        studentsHash[stu.id] = {
            "access_token": create_access_token(stu.id),
            "token_type": "token"
        }
        studentsPassword[stu.id] = hashPassword(stu.password)
        return stu

@app.post("/students/login")
def login(stu: StudentLogin):
    if stu.id not in students or not bcrypt.checkpw(stu.password.encode("utf-8"), studentsPassword[stu.id]):
        return {"detail": "Invalid id or password"}
    else:
        return studentsHash[stu.id]

@app.post("/students/newsecret")
def newSecret(s: Secret, req: Request):
    token = req.headers.get("Authorization")
    if token:
        for i in studentsHash:
            if studentsHash[i]["access_token"] == token:
                students[i]["secret"] = s.secret
                return s
    return {"detail": "Access denied"}