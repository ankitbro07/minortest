Objective:
Create a basic FastAPI project to manage student records using JSON file storage.

Requirements
1. Project Setup 
Create a folder named:
student_api_project
Inside it create:
main.py
students.json
requirements.txt
README.md
Install required packages and prepare project environment.

Use students.json file to store student data.
Each student record should contain:
{
 "id": 1,
 "name": "Rahul",
 "course": "Python",
 "marks": 85
}
Use file handling to:
Read data from file
Write data to file
Update data in file

3. FastAPI Endpoints (20 Marks)
Create following APIs:
Home Route
/
Response:
{"message":"Welcome to Student API"}

Get All Students
/students
Return all student records.

Add New Student
POST /students
Input:
{
 "id": 2,
 "name": "Riya",
 "course": "FastAPI",
 "marks": 90
}

Search Student by ID
/students/{id}

Delete Student
DELETE /students/{id}

Additional Features Using Python 
Show current date and time when a student is added
Count total number of students stored


Git & GitHub Submission
Initialize your project using Git
Track project files
Commit your project with proper message
Create a GitHub repository
Upload your complete project to your GitHub account


