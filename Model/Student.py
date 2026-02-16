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


stud1 = Student(2880, "Thom", "Thom@Gmail.Com", 23, 2, ["Python", "Java", "Github", "Git", "Agile"])

print(stud1)