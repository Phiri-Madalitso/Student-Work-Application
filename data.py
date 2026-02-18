# Datalag for Student-Work-Application
# Hva: Eier lister (iterasjon/filtering/sortering) og dicts (O(1)-oppslag på ID).
# Hvorfor: Oppgaven krever begge strukturer; samlet ett sted unngår duplisering og sirkulære importer.

from Model.Company import Company
from Model.Student import Student
from Model.Jobs import Job

# --- Steg 1: Lister og dicts ---
students = []
students_by_id = {}
companies = []
companies_by_id = {}
jobs = []
jobs_by_id = {}


# --- Steg 2: Registrering ---
def register_student(student_id: int, name: str, email: str, skills: list, age: int = None, year: int = None):
    """Oppretter en student og lagrer i både liste og dict. Returnerer studenten."""
    student = Student(student_id=student_id, name=name, email=email, skills=skills, age=age, year=year)
    students.append(student)
    students_by_id[student_id] = student
    return student


def register_company(company_id: int, name: str, email: str):
    """Oppretter en bedrift og lagrer i både liste og dict. Returnerer bedriften."""
    company = Company(company_id=company_id, name=name, email=email)
    companies.append(company)
    companies_by_id[company_id] = company
    return company


# --- Steg 3: Opprette jobb ---
def create_job(job_id: int, title: str, description: str, required_skills: list, budget: int, company_id: int, status: str = "open"):
    """Bedrift publiserer en oppgave. Oppslag på company_id er O(1). Returnerer jobben eller None."""
    company = companies_by_id.get(company_id)
    if company is None:
        return None
    job = Job(job_id=job_id, description=description, title=title, required_skills=required_skills, budget=budget, status=status, company=company)
    jobs.append(job)
    jobs_by_id[job_id] = job
    return job


# --- Steg 4: Oppslag på ID (O(1)) ---
def get_student_by_id(student_id):
    return students_by_id.get(student_id)


def get_company_by_id(company_id):
    return companies_by_id.get(company_id)


def get_job_by_id(job_id):
    return jobs_by_id.get(job_id)


# --- Steg 5: Matching (O(n) i antall jobber) ---
def find_matching_jobs_for_student(student_id):
    """Returnerer åpne jobber der minst ett required_skill matcher studentens skills."""
    student = get_student_by_id(student_id)
    if student is None:
        return []
    student_skills = set(student.skills)
    return [
        job for job in jobs
        if job.status == "open" and (set(job.required_skills) & student_skills)
    ]


def find_students_for_job(job_id):
    """Returnerer studenter som matcher jobbens required_skills."""
    job = get_job_by_id(job_id)
    if job is None:
        return []
    required = set(job.required_skills)
    return [s for s in students if set(s.skills) & required]


# --- Steg 6: Sortering etter budget (O(n log n)) ---
def get_jobs_sorted_by_budget(only_open: bool = True):
    """Returnerer jobber sortert på budget. only_open=True gir kun åpne (O(n) filter + O(n log n) sort)."""
    to_sort = [j for j in jobs if j.status == "open"] if only_open else list(jobs)
    return sorted(to_sort, key=lambda j: j.budget)
