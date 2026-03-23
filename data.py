# Data layer for Student-Work-Application
# What: Owns lists (iteration/filtering/sorting) and dicts (O(1) lookup on ID).
# Why: The assignment requires both structures; keeping them in one place avoids duplication and circular imports.

from Model.Company import Company
from Model.Student import Student
from Model.Jobs import Job

# --- Step 1: Lists and dicts ---
students = []
students_by_id = {}
companies = []
companies_by_id = {}
jobs = []
jobs_by_id = {}


# --- Step 2: Registration ---
def register_student(student_id: int, name: str, email: str, skills: list, age: int = None, year: int = None):
    """Create a student and store it in both list and dict. Returns the student."""
    if student_id in students_by_id:
        raise ValueError(f"Student ID {student_id} already exists.")
    student = Student(student_id=student_id, name=name, email=email, skills=skills, age=age, year=year)
    students.append(student)
    students_by_id[student_id] = student
    return student


def register_company(company_id: int, name: str, email: str):
    """Create a company and store it in both list and dict. Returns the company."""
    if company_id in companies_by_id:
        raise ValueError(f"Company ID {company_id} already exists.")
    company = Company(company_id=company_id, name=name, email=email)
    companies.append(company)
    companies_by_id[company_id] = company
    return company


# --- Step 3: Create job ---
def create_job(job_id: int, title: str, description: str, required_skills: list, budget: int, company_id: int, status: str = "open"):
    """Company publishes a job. Lookup on company_id is O(1). Returns the job or None."""
    if job_id in jobs_by_id:
        raise ValueError(f"Job ID {job_id} already exists.")
    company = companies_by_id.get(company_id)
    if company is None:
        return None
    job = Job(job_id=job_id, description=description, title=title, required_skills=required_skills, budget=budget, status=status, company=company)
    jobs.append(job)
    jobs_by_id[job_id] = job
    return job


# --- Step 4: Lookup by ID (O(1)) ---
def get_student_by_id(student_id):
    return students_by_id.get(student_id)


def get_company_by_id(company_id):
    return companies_by_id.get(company_id)


def get_job_by_id(job_id):
    return jobs_by_id.get(job_id)


# --- Step 5: Matching (O(n) in number of jobs) ---
def find_matching_jobs_for_student(student_id):
    """Return open jobs where at least one required_skill matches the student's skills."""
    student = get_student_by_id(student_id)
    if student is None:
        return []
    student_skills = set(student.skills)
    return [
        job for job in jobs
        if job.status == "open" and (set(job.required_skills) & student_skills)
    ]


def find_students_for_job(job_id):
    """Return students that match the job's required_skills."""
    job = get_job_by_id(job_id)
    if job is None:
        return []
    required = set(job.required_skills)
    return [s for s in students if set(s.skills) & required]


# --- Step 6: Sorting by budget (O(n log n)) ---
def get_jobs_sorted_by_budget(only_open: bool = True):
    """Return jobs sorted by budget. only_open=True returns only open jobs (O(n) filter + O(n log n) sort)."""
    to_sort = [j for j in jobs if j.status == "open"] if only_open else list(jobs)
    return sorted(to_sort, key=lambda j: j.budget)
