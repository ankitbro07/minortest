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


Implement any two of the following:
Show current date and time when a student is added
Generate random student ID automatically
Count total number of students stored
Display project folder/file existence check
Calculate average marks of all students

Initialize your project using Git
Track project files
Commit your project with proper message
Create a GitHub repository
Upload your complete project to your GitHub account



