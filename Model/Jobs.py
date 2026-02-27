from .Company import Company


class Job:
    """En oppgave publisert av en bedrift. Brukes ved matching og sortering."""

    def __init__(self, job_id: int, description: str, title: str, required_skills: list, budget: int, status: str, company: Company):
        self.job_id = job_id
        self.description = description
        self.title = title
        self.required_skills = required_skills
        self.budget = budget
        self.status = status
        self.company = company

    def __repr__(self):
        return f"Job({self.job_id}, {self.title}, {self.required_skills}, {self.budget}, {self.status})"
