# === Import === #

import persistent
from persistent.list import PersistentList
from typing import Optional, TypedDict
from fastapi import FastAPI, Header, HTTPException, Depends
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer
from random import randint
from contextlib import asynccontextmanager
import BTrees._OOBTree
import ZODB, ZODB.FileStorage
import transaction
import bcrypt
from zope.interface.interface import ro

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")





# === BackEnd Util Functions === #

def gen_token(id: int) -> str:
    global root
    token_user = root.token_user
    for token in  token_user:
        if token_user[token] == id:
            return token 
    token = "%020x" % (randint(0, 0xfffffffffffffffffffff))
    while token in token_user:
        token = "%020x" % (randint(0, 0xfffffffffffffffffffff))
    token_user[token] = id
    transaction.commit()
    return token

def verify_token(token: str) -> Optional[int]:
    global root
    token = token.lower()
    token_user = root.token_user
    if token in token_user:
        return token_user[token]
    return None

async def get_current_user(authorization: str = Header(...)) -> Optional["Student"]:
    global root
    if not authorization.startswith("token "):
        raise HTTPException(status_code=401, detail="Invalid Auth Header")
    token = authorization[len("token "):].strip()
    id = verify_token(token)
    if not id:
        raise HTTPException(status_code=404, detail="Invalid or expired Token")
    user_db = root.students
    if id not in user_db:
        raise HTTPException(status_code=401, detail="User not found")
    user_record = user_db[id]
    return user_record.getDetail()

def hash_password(password: str):
    temp = password.encode("utf-8")
    return bcrypt.hashpw(temp, bcrypt.gensalt()).decode("utf-8")

def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))





# === FastAPI === #

# === FastAPI BaseModel === #

class StudentBM(BaseModel):
    id: int
    name: str
    password: str

class StudentLogin(BaseModel):
    id: int
    password: str

class EnrollmentBM(BaseModel):
    id: int
    score: int


# === FastAPI init and cleanup === #

def startup_event():
    global db, root
    storage = ZODB.FileStorage.FileStorage("mein_data.fs")
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root()

    if not hasattr(root, "courses"):
        root.courses = BTrees._OOBTree.BTree()
        root.courses[101] = Course(101, "Computer Programming", 4)
        root.courses[201] = Course(201, "Web Programmin", 4)
        root.courses[202] = Course(202, "Software Engineering Principle", 5)
        root.courses[301] = Course(301, "Artificial Intelligent", 3)

        root.courses[101].setGradeScheme([
                {"Grade": "A", "min": 90, "max": 100},
                {"Grade": "B", "min": 80, "max": 89},
                {"Grade": "C", "min": 70, "max": 79},
                {"Grade": "D", "min": 60, "max": 69},
                {"Grade": "F", "min": 0, "max": 59},
        ])

    
    if not hasattr(root, "students"):
            root.students = BTrees._OOBTree.BTree()
            root.students[1103] = Student(1103, "Man the man", hash_password("man so cool"))
            root.students[1103].enrollCourse(root.courses[101]).setScore(101)
            root.students[1103].enrollCourse(root.courses[201]).setScore(69)
            root.students[1103].enrollCourse(root.courses[202]).setScore(34)
            root.students[1103].enrollCourse(root.courses[301]).setScore(56)
    
    if not hasattr(root, "token_user"):
        root.token_user = BTrees._OOBTree.BTree()

    app.state.connection = connection


def shutdown_event():
    global db
    connection = getattr(app.state, "connection", None)
    if connection:
        connection.close()
    db.close()

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.title = "Student API"
    startup_event()

    yield

    shutdown_event()

app = FastAPI(lifespan=lifespan)





# === FastAPI routes === #

# === route / === #

@app.get("/")
async def helloRoot():
    return {"message": "Hello world"}

@app.get("/student/all")
async def getAllStudents():
    data = {}
    students = root.students
    for student in students:
        tmp = students[student]
        data[student] = tmp.getDetail()
        data[student].pop("password")
    return data

# === route /student === #

@app.post("/student/new")
async def student_new(stu: StudentBM):
    students = root.students
    if stu.id in students:
        raise HTTPException(status_code=400, detail="Student exists")
    students[stu.id] = Student(stu.id, stu.name, password=hash_password(stu.password))
    transaction.commit()
    tmp = students[stu.id].getDetail()
    tmp.pop("password")
    return tmp

@app.post("/student/login")
async def student_login(stu: StudentLogin):
    students = root.students
    if stu.id not in students:
        raise HTTPException(status_code=400, detail="Invalid Username or password")
    user_record = students[stu.id].getDetail()
    if not verify_password(stu.password, user_record["password"]):
        raise HTTPException(status_code=400, detail="Invalid Username or password")
    token = gen_token(user_record["id"])
    return { "access_token": token, "token_type": "token" }

@app.post("/student/enroll")
async def student_enroll(subj: EnrollmentBM, cur_user:dict = Depends(get_current_user)):
    global root
    student_id = cur_user["id"]
    student = root.students[student_id]
    courses = root.courses
    if subj.id not in courses:
        raise HTTPException(status_code=404, detail=f"Course ID {subj.id} not found")
    course_to_enroll = courses[subj.id]
    if student.getEnrollment(course_to_enroll):
        raise HTTPException(status_code=400, detail=f"{cur_user["name"]} already enrolled this course")
    student.enrollCourse(course_to_enroll).setScore(subj.score)
    return {"message": f"Successfully enrolled {student.name} in {course_to_enroll.name}"}


@app.get("/student/enrollinfo")
async def student_enrollinfo(cur_user: dict = Depends(get_current_user)):
    global root
    student = root.students[cur_user["id"]]
    result = []
    for e in student.enrolls:
        result.append(e.getDetail())
    return result

@app.get("/student/transcript")
async def student_transcript(cur_user: dict = Depends(get_current_user)):
    global root
    student = root.students[cur_user["id"]]
    return student.getTranscript()

@app.get("/student/transcript/html", response_class=HTMLResponse)
async def student_transcript_html(cur_user: dict = Depends(get_current_user)):
    global root
    student = root.students[cur_user["id"]]
    transcript = student.getTranscript()
    result = f"""
    <html>
        <body>
            <h1>Unofficial Transcript</h1>
            <h2>Student ID: {transcript["id"]}</h2>
            <h2>Name: {transcript["name"]}</h2>
            <table border="1">
                <thead>
                    <tr>
                        <th>Course ID</th>
                        <th>Title</th>
                        <th>Credit</th>
                        <th>Score</th>
                        <th>Grade</th>
                    </tr>
                </thead>
                <tbody>
    """

    for en in transcript["enroll"]:
        result += f"""
                        <tr>
                            <td>{en["id"]}</td>
                            <td>{en["name"]}</td>
                            <td>{en["credit"]}</td>
                            <td>{en["score"]}</td>
                            <td>{en["grade"]}</td>
                        </tr>
        """

    fmt_gpa = format(transcript["gpa"], ".2f")

    result += f"""
                </tbody>
                </thead>
            </table>
            <h3>GPA: {fmt_gpa}</h3>

        </body>
    </html>
    """
    return result



@app.post("/student/logout")
async def student_logout(cur_user: dict = Depends(get_current_user)):
    id = cur_user["id"]
    token_user = root.token_user
    for token in token_user:
        if token in token_user:
            if token_user[token] == id:
                del token_user[token]
        return {"message": f"Bye {cur_user["name"]}"}

# === route /course === #

@app.get("/course")
async def course_root():
    global root
    result = dict()
    for (k, v) in root.courses.items():
        result[k] = v
    return result

@app.get("/course/html", response_class=HTMLResponse)
async def course_html():
    global root
    result = """
    <html>
        <body>
            <h1>Courses</h1>
            <table border="1">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Credit</th>
                    </tr>
                </thead>
                <tbody>
    """

    for c in root.courses.keys():
        result += f"""
                        <tr>
                            <td>{root.courses[c].id}</td>
                            <td>{root.courses[c].name}</td>
                            <td>{root.courses[c].credit}</td>
                        </tr>
        """

    result += """
                </tbody>
                </thead>
            </table>
        </body>
    </html>
    """
    return result





# === ZODB === #

# === Util TypedDict === #

class EnrollmentGetDetailResult(TypedDict):
    id: int
    name: str
    credit: int
    score: float
    grade: str


class TranscriptGetResult(TypedDict):
    id: int
    name: str
    enroll: list[EnrollmentGetDetailResult]
    gpa: float

# === Classes === #

class Student(persistent.Persistent):
    def __init__(self, student_id: int, name: str, password: str = "") -> None:
        self.enrolls = PersistentList()
        self.id = student_id
        self.name = name
        self.password = password

    def getDetail(self):
        enroll = []
        for e in self.enrolls:
            enroll.append(e.getDetail())

        return {
            "id": self.id,
            "name": self.name,
            "password": self.password,
            "enroll": enroll,
            "gpa": self.getGPA()
        }
        
    def enrollCourse(self, course: "Course") -> "Enrollment":
        e = Enrollment(course = course, student = self)
        self.enrolls.append(e)
        return e
    
    def getEnrollment(self, course) -> Optional["Enrollment"]:
        for e in self.enrolls:
            if e.course == course:
                return e
        return None

    def getTranscript(self) -> TranscriptGetResult:
        enroll = []
        for e in self.enrolls:
            enroll.append(e.getDetail())
        return {
            "id": self.id,
            "name": self.name,
            "enroll": enroll,
            "gpa": self.getGPA()
        }

    def printTranscript(self) -> None:
        print("<-=- Transcript -=->")
        print(f"ID: {self.id:<6} Name: {self.name}")
        print("Course list")
        for e in self.enrolls:
            e.printDetail()
        gpa = self.getGPA()
        print(f"Total GPA is: {gpa:.2f}")   

    def getGPA(self) -> float:
        numerator = 0
        denominator = 0
        for e in self.enrolls:
            text = e.getGrade()
            if text == "A":
                numerator += 4 * e.course.getCredit()
                denominator += e.course.getCredit()
            # elif text == "B+":
            #     numerator += 3.5 * e.course.getCredit()
                # denominator += e.course.getCredit()
            elif text == "B":
                numerator += 3 * e.course.getCredit()
                denominator += e.course.getCredit()
            # elif text == "C+":
            #     numerator += 2.5 * e.course.getCredit()
            #     denominator += e.course.getCredit()
            elif text == "C":
                numerator += 2 * e.course.getCredit()
                denominator += e.course.getCredit()
            # elif text == "D+":
            #     numerator += 1.5 * e.course.getCredit()
            #     denominator += e.course.getCredit()
            elif text == "D":
                numerator += 1 * e.course.getCredit()
                denominator += e.course.getCredit()
            else:
                denominator += e.course.getCredit()
        if denominator == 0:
            return 0
        else:
            return numerator/denominator
        
    def setName(self, name: str) -> None:
        self.name = name

class Enrollment(persistent.Persistent):
    def __init__(self, course: "Course", student: Student, score = 0) -> None:
        self.course = course
        self.student = student
        self.score = score
    
    def getCourse(self) -> "Course":
        return self.course
    

    def getGrade(self) -> str:
        return self.course.scoreGrading(self.score)

    def getScore(self) -> int:
        return self.score
    
    def printDetail(self) -> None:
        print(f"ID: {self.course.id:<6} Course: {self.course.name:<30} "
         f"Credit: {self.course.getCredit():<2} Score: {self.getScore():<2} Grade: {self.getGrade():<2}")

    def getDetail(self) -> EnrollmentGetDetailResult:
        return {
            "id": self.course.id,
            "name": self.course.name,
            "credit": self.course.credit,
            "score": self.getScore(),
            "grade": self.getGrade()
        }
    
    def setScore(self, score: int) -> None:
        self.score = score


class Course (persistent.Persistent):
    def __init__(self, id, name: str = "", credit: int = 0) -> None:
        self.id = id
        self.name = name 
        self.credit = credit
        self.grading = [
            {"Grade": "A", "min": 80, "max": 100},
            {"Grade": "B", "min": 70, "max": 79},
            {"Grade": "C", "min": 60, "max": 69},
            {"Grade": "D", "min": 50, "max": 59},
            {"Grade": "F", "min": 0, "max": 49},
        ]
        
    def __str__(self) -> str:
        return f"ID: {self.id:<6} Course: {self.name:<30} Credit: {self.credit:<2}"
    
    def setName(self, name: str) -> None:
        self.name = name

    def getCredit(self) -> int:
        return self.credit

    def printDetail(self) -> None:
        print(self.__str__())

    def scoreGrading(self, score) -> str:
        for g in self.grading:
            if g["min"] <= score and score <= g["max"]:
                return g["Grade"]
        return "F"

    def setGradeScheme(self, scheme: list) -> None:
        self.grading = scheme
