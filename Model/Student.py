class Student:
    """En IT-student som kan matche mot oppgaver. Skills brukes ved matching."""

    def __init__(self, student_id: int, name: str, email: str, skills: list, age: int = None, year: int = None):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.skills = skills
        self.age = age
        self.year = year

    def __repr__(self):
        return f"Student({self.student_id}, {self.name}, {self.email}, {self.skills})"

    def show_skills(self):
        return f"{self.name}'s skills: {', '.join(self.skills)}"