from Company import Company, comp1

class Jobs:
    def __init__(self, jobs_id: int, description: str, title: str, required_skills: list, budget: int, status: str, company: Company):
        self.jobs_id = jobs_id
        self.description = description
        self.title = title
        self.required_skills = required_skills
        self.budget = budget
        self.status = status
        self.company = company

    def __repr__(self):
        return f"Jobs({self.jobs_id}, {self.description}, {self.title}, {self.required_skills}, {self.budget}, {self.status}, {self.company})"
        
job1 = Jobs(1001, "Looking for a Python developer to build a web application.", "Python Developer", ["Python", "Django", "REST API"], 5000, "Open", comp1)
job2 = Jobs(1002, "Seeking a Java developer for a mobile app project.", "Java Developer", ["Java", "Android", "Git"], 4000, "Open", comp1)
job3 = Jobs(1003, "Need a C# developer for a desktop application.", "C# Developer", ["C#", ".NET", "SQL"], 4500, "Closed", comp1)

all_jobs = [job1, job2, job3]
