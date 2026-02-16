from Jobs import *

class Student:
    def __init__(self, student_id: int, name: str, email: str, age: int, year: int, skills: list):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.age = age
        self.year = year
        self.skills = skills

    def __repr__(self):
        return f"Student({self.student_id}, {self.name}, {self.email}, {self.age}, {self.year}, {self.skills})"
    
    def show_skills(self):
        return f"{self.name}'s skills: {', '.join(self.skills)}"
    
    def show_jobs(self):
        return [
            job for job in all_jobs
            if set(job.required_skills) & set(self.skills)
        ]



stud1 = Student(2880, "Thom", "Thom@Gmail.Com", 23, 2, ["Python", "C#", "Agile"])
print(stud1)

show_skills = stud1.show_skills()
print(show_skills)

relevant_jobs = stud1.show_jobs()
print("Relevant jobs for Thom:")
for job in relevant_jobs:
    print(job)