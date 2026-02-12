class Student:
    def __init__(self, student_id: id, name: str, age: int, year: int, skills: list):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.year = year
        self.skills = skills

    def __repr__(self):
        return f"Student({self.student_id}, {self.name}, {self.age}, {self.year}, {self.skills})"


stud1 = Student(2880, "Thom", 23, 2, ["Python", "Java", "Github", "Git", "Agile", "Scrum"])

print(stud1)