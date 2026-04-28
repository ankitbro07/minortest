#Read data from file
with open("students.json","r") as f:
    print(f.read())

#Write data to file
with open("students.json","w") as f: 
    f.write("this are the recodes of the students")

#Update data in file
with open("students.json","r") as f:
      print({
 "id": 1,
 "name": "Rahul",
 "course": "Python",
 "marks": 85
})


#FastAPI Endpoints()##########3

from fastapi import FastAPI
import os
import json
app=FastAPI()
@app.get("/")
def home_route():
     return{"message":"Welcome to Student API"}

app=FastAPI()
@app.post("/students")
def students_record():
     return{"Return all student records."}


app=FastAPI()
@app.post(" /students" )
def add():
     return{
 "id": 2,
 "name": "Riya",
 "course": "FastAPI",
 "marks": 90
}


app=FastAPI()
@app.get("/students")
def students_record():
     return{"Return all student records."}


app=FastAPI()
@app.post("/students")
def students_record():
     return{"id of the student"}


app=FastAPI()
@app.delete("/students/{id}")
def students():
     return{"id is deleted"}


app=FastAPI()
@app.post("/datetime")
def students(datetime):
     return{{
 "id": 1,
 "name": "Rahul",
 "course": "Python",
 "marks": 85,
  "time":datetime.now
}
}

app=FastAPI()
@app.post("/students/{id}")
def students():
     return{{
 "id": 1,
 "name": "Rahul",
 "course": "Python",
 "marks": 85
}
}
