# Main.py – entry point for Student-Work-Application
# Run from the project folder: python Main.py
# Interactive menu: registration, create job, matching, sorting, lists.

import data


# --- Formatting helpers (clean display) ---

def format_company(c):
    """Readable text for a company."""
    return f"Company {c.company_id}: {c.name} ({c.email})"


def format_student(s):
    """Readable text for a student."""
    skills_str = ", ".join(s.skills) if s.skills else "(none)"
    return f"Student {s.student_id}: {s.name} – {s.email} – {skills_str}"


def format_job(j):
    """Readable text for a job."""
    skills_str = ", ".join(j.required_skills) if j.required_skills else "(none)"
    return f"Job {j.job_id}: {j.title} – {j.budget} NOK – status: {j.status} – {skills_str}"


# --- Helper for reading integers (error handling) ---

def input_int(prompt):
    """Read an integer; return None on invalid input."""
    try:
        s = input(prompt).strip()
        if not s:
            return None
        return int(s)
    except ValueError:
        return None


# --- Demo data (menu option 10) ---

def run_demo():
    """Fill the system with demo data. Recommended to use only once."""
    if data.students or data.companies or data.jobs:
        print("Data already exists. Filling with demo data should only be done once.")
        return
    data.register_company(101, "Tech Solutions Inc.", "contact@techsolutions.com")
    data.register_student(2880, "Thom", "Thom@Gmail.Com", ["Python", "C#", "Agile"], age=23, year=2)
    data.register_student(2881, "Kari", "kari@stud.ntnu.no", ["Java", "Git"])
    data.create_job(1001, "Python Developer", "Looking for a Python developer to build a web application.", ["Python", "Django", "REST API"], 5000, 101)
    data.create_job(1002, "Java Developer", "Seeking a Java developer for a mobile app project.", ["Java", "Android", "Git"], 4000, 101)
    data.create_job(1003, "C# Developer", "Need a C# developer for a desktop application.", ["C#", ".NET", "SQL"], 4500, 101, status="Closed")
    print("Demo data added: 1 company, 2 students, 3 jobs.")
    for c in data.companies:
        print(" ", format_company(c))
    for s in data.students:
        print(" ", format_student(s))
    for j in data.jobs:
        print(" ", format_job(j))


def menu_register_student():
    """Menu option 1: Register student."""
    student_id = input_int("Student ID (number): ")
    if student_id is None:
        print("Invalid number. Please try again.")
        return
    if data.get_student_by_id(student_id):
        print(f"Student with ID {student_id} already exists.")
        return
    name = input("Name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    email = input("Email: ").strip()
    if not email:
        print("Email cannot be empty.")
        return
    skills_str = input("Skills (comma separated, e.g. Python, Java): ").strip()
    skills = [s.strip() for s in skills_str.split(",") if s.strip()] if skills_str else []
    student = data.register_student(student_id, name, email, skills)
    print("Registered:", format_student(student))


def menu_register_company():
    """Menu option 2: Register company."""
    company_id = input_int("Company ID (number): ")
    if company_id is None:
        print("Invalid number. Please try again.")
        return
    if data.get_company_by_id(company_id):
        print(f"Company with ID {company_id} already exists.")
        return
    name = input("Company name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    email = input("Email: ").strip()
    if not email:
        print("Email cannot be empty.")
        return
    company = data.register_company(company_id, name, email)
    print("Registered:", format_company(company))


def menu_create_job():
    """Menu option 3: Create job."""
    if not data.companies:
        print("No companies registered. Choose 2 to register a company first, then you can create jobs.")
        return
    job_id = input_int("Job ID (number): ")
    if job_id is None:
        print("Invalid number. Please try again.")
        return
    if data.get_job_by_id(job_id):
        print(f"Job with ID {job_id} already exists.")
        return
    title = input("Title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return
    description = input("Description: ").strip()
    skills_str = input("Required skills (comma separated): ").strip()
    required_skills = [s.strip() for s in skills_str.split(",") if s.strip()] if skills_str else []
    budget = input_int("Budget (number): ")
    if budget is None:
        print("Invalid budget. Please try again.")
        return
    print("Existing companies:", ", ".join(f"{c.company_id} ({c.name})" for c in data.companies))
    company_id = input_int("Company ID: ")
    if company_id is None:
        print("Invalid company ID. Please try again.")
        return
    if data.get_company_by_id(company_id) is None:
        print(f"Company with ID {company_id} does not exist. Use an ID from the list above.")
        return
    status = input("Status (Enter = open, for example open/closed): ").strip() or "open"
    job = data.create_job(job_id, title, description, required_skills, budget, company_id, status=status)
    if job:
        print("Created:", format_job(job))
        print("List all jobs with option 9.")
    else:
        print("Could not create job.")


def menu_matching_jobs_for_student():
    """Menu option 4: Show matching jobs for a student."""
    student_id = input_int("Student ID: ")
    if student_id is None:
        print("Invalid number. Please try again.")
        return
    student = data.get_student_by_id(student_id)
    if student is None:
        print("Student not found.")
        return
    matching = data.find_matching_jobs_for_student(student_id)
    print(f"Matching jobs for {student.name} ({student_id}):")
    if not matching:
        print("  No open jobs match the student's skills.")
    else:
        for j in matching:
            print(" ", format_job(j))


def menu_jobs_sorted_by_budget():
    """Menu option 5: Show open jobs sorted by budget."""
    jobs = data.get_jobs_sorted_by_budget(only_open=True)
    print("Open jobs sorted by budget (low to high):")
    if not jobs:
        print("  No open jobs.")
    else:
        for j in jobs:
            print(" ", format_job(j))


def menu_students_for_job():
    """Menu option 6: Show students that match a job."""
    job_id = input_int("Job ID: ")
    if job_id is None:
        print("Invalid number. Please try again.")
        return
    job = data.get_job_by_id(job_id)
    if job is None:
        print("Job not found.")
        return
    students = data.find_students_for_job(job_id)
    print(f"Students that match job {job_id} ({job.title}):")
    if not students:
        print("  No students match.")
    else:
        for s in students:
            print(" ", format_student(s))


def menu_list_students():
    """Menu option 7: List all students."""
    if not data.students:
        print("No students registered yet.")
        return
    print("All students:")
    for s in data.students:
        print(" ", format_student(s))


def menu_list_companies():
    """Menu option 8: List all companies."""
    if not data.companies:
        print("No companies registered yet.")
        return
    print("All companies:")
    for c in data.companies:
        print(" ", format_company(c))


def menu_list_jobs():
    """Menu option 9: List all jobs."""
    if not data.jobs:
        print("No jobs created yet.")
        return
    print("All jobs:")
    for j in data.jobs:
        print(" ", format_job(j))


def show_menu():
    """Print the main menu."""
    print("\n--- Student-Work-Application ---")
    print("1. Register student")
    print("2. Register company")
    print("3. Create job")
    print("4. Show matching jobs for a student")
    print("5. Show open jobs sorted by budget")
    print("6. Show students that match a job")
    print("7. List all students")
    print("8. List all companies")
    print("9. List all jobs")
    print("10. Fill with demo data")
    print("0. Exit")


def main():
    """Main loop: show menu and handle choices."""
    while True:
        show_menu()
        choice = input("Choose: ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "1":
            menu_register_student()
        elif choice == "2":
            menu_register_company()
        elif choice == "3":
            menu_create_job()
        elif choice == "4":
            menu_matching_jobs_for_student()
        elif choice == "5":
            menu_jobs_sorted_by_budget()
        elif choice == "6":
            menu_students_for_job()
        elif choice == "7":
            menu_list_students()
        elif choice == "8":
            menu_list_companies()
        elif choice == "9":
            menu_list_jobs()
        elif choice == "10":
            run_demo()
        else:
            print("Invalid choice. Choose 0–10.")


if __name__ == "__main__":
    main()
