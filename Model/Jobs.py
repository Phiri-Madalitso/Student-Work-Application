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
print(job1)
print("Hello!")