# Main.py – inngangspunkt for Student-Work-Application
# Kjør fra prosjektmappen: python Main.py
# Interaktiv meny: registrering, opprett jobb, matching, sortering, lister.

import data
from Model.Company import Company
from Model.Student import Student
from Model.Jobs import Job


# --- Formateringshjelpere (ryddig visning) ---

def format_company(c):
    """Lesbar tekst for en bedrift."""
    return f"Bedrift {c.company_id}: {c.name} ({c.email})"


def format_student(s):
    """Lesbar tekst for en student."""
    skills_str = ", ".join(s.skills) if s.skills else "(ingen)"
    return f"Student {s.student_id}: {s.name} – {s.email} – {skills_str}"


def format_job(j):
    """Lesbar tekst for en jobb."""
    skills_str = ", ".join(j.required_skills) if j.required_skills else "(ingen)"
    return f"Jobb {j.job_id}: {j.title} – {j.budget} kr – status: {j.status} – {skills_str}"


# --- Hjelp for å lese tall (feilhåndtering) ---

def input_int(prompt):
    """Les et heltall; returnerer None ved ugyldig input."""
    try:
        s = input(prompt).strip()
        if not s:
            return None
        return int(s)
    except ValueError:
        return None


# --- Demonstrasjonsdata (menypunkt 10) ---

def run_demo():
    """Fyll systemet med demodata. Anbefales kun brukt én gang."""
    if data.students or data.companies or data.jobs:
        print("Det finnes allerede data. Fyll med demodata bør bare brukes én gang.")
        return
    data.register_company(101, "Tech Solutions Inc.", "contact@techsolutions.com")
    data.register_student(2880, "Thom", "Thom@Gmail.Com", ["Python", "C#", "Agile"], age=23, year=2)
    data.register_student(2881, "Kari", "kari@stud.ntnu.no", ["Java", "Git"])
    data.create_job(1001, "Python Developer", "Looking for a Python developer to build a web application.", ["Python", "Django", "REST API"], 5000, 101)
    data.create_job(1002, "Java Developer", "Seeking a Java developer for a mobile app project.", ["Java", "Android", "Git"], 4000, 101)
    data.create_job(1003, "C# Developer", "Need a C# developer for a desktop application.", ["C#", ".NET", "SQL"], 4500, 101, status="Closed")
    print("Demodata lagt inn: 1 bedrift, 2 studenter, 3 jobber.")
    for c in data.companies:
        print(" ", format_company(c))
    for s in data.students:
        print(" ", format_student(s))
    for j in data.jobs:
        print(" ", format_job(j))


def menu_register_student():
    """Menypunkt 1: Registrer student."""
    student_id = input_int("Student-ID (tall): ")
    if student_id is None:
        print("Ugyldig tall. Prøv igjen.")
        return
    if data.get_student_by_id(student_id):
        print(f"Student med ID {student_id} finnes allerede.")
        return
    name = input("Navn: ").strip()
    if not name:
        print("Navn kan ikke være tomt.")
        return
    email = input("E-post: ").strip()
    if not email:
        print("E-post kan ikke være tom.")
        return
    skills_str = input("Ferdigheter (kommaseparert, f.eks. Python, Java): ").strip()
    skills = [s.strip() for s in skills_str.split(",") if s.strip()] if skills_str else []
    student = data.register_student(student_id, name, email, skills)
    print("Registrert:", format_student(student))


def menu_register_company():
    """Menypunkt 2: Registrer bedrift."""
    company_id = input_int("Bedrifts-ID (tall): ")
    if company_id is None:
        print("Ugyldig tall. Prøv igjen.")
        return
    if data.get_company_by_id(company_id):
        print(f"Bedrift med ID {company_id} finnes allerede.")
        return
    name = input("Bedriftsnavn: ").strip()
    if not name:
        print("Navn kan ikke være tomt.")
        return
    email = input("E-post: ").strip()
    if not email:
        print("E-post kan ikke være tom.")
        return
    company = data.register_company(company_id, name, email)
    print("Registrert:", format_company(company))


def menu_create_job():
    """Menypunkt 3: Opprett jobb."""
    if not data.companies:
        print("Ingen bedrifter registrert. Velg 2 for å registrere en bedrift først, deretter kan du opprette jobber.")
        return
    job_id = input_int("Jobb-ID (tall): ")
    if job_id is None:
        print("Ugyldig tall. Prøv igjen.")
        return
    if data.get_job_by_id(job_id):
        print(f"Jobb med ID {job_id} finnes allerede.")
        return
    title = input("Tittel: ").strip()
    if not title:
        print("Tittel kan ikke være tom.")
        return
    description = input("Beskrivelse: ").strip()
    skills_str = input("Krevede ferdigheter (kommaseparert): ").strip()
    required_skills = [s.strip() for s in skills_str.split(",") if s.strip()] if skills_str else []
    budget = input_int("Budget (tall): ")
    if budget is None:
        print("Ugyldig budget. Prøv igjen.")
        return
    print("Eksisterende bedrifter:", ", ".join(f"{c.company_id} ({c.name})" for c in data.companies))
    company_id = input_int("Bedrifts-ID: ")
    if company_id is None:
        print("Ugyldig bedrifts-ID. Prøv igjen.")
        return
    if data.get_company_by_id(company_id) is None:
        print(f"Bedrift med ID {company_id} finnes ikke. Bruk en ID fra listen over.")
        return
    status = input("Status (Enter = open, eller f.eks. open/closed): ").strip() or "open"
    job = data.create_job(job_id, title, description, required_skills, budget, company_id, status=status)
    if job:
        print("Opprettet:", format_job(job))
        print("List alle jobber med valg 9.")
    else:
        print("Kunne ikke opprette jobb.")


def menu_matching_jobs_for_student():
    """Menypunkt 4: Vis matchende jobber for en student."""
    student_id = input_int("Student-ID: ")
    if student_id is None:
        print("Ugyldig tall. Prøv igjen.")
        return
    student = data.get_student_by_id(student_id)
    if student is None:
        print("Student ikke funnet.")
        return
    matching = data.find_matching_jobs_for_student(student_id)
    print(f"Matchende jobber for {student.name} ({student_id}):")
    if not matching:
        print("  Ingen åpne jobber matcher studentens ferdigheter.")
    else:
        for j in matching:
            print(" ", format_job(j))


def menu_jobs_sorted_by_budget():
    """Menypunkt 5: Vis åpne jobber sortert på budget."""
    jobs = data.get_jobs_sorted_by_budget(only_open=True)
    print("Åpne jobber sortert på budget (lav til høy):")
    if not jobs:
        print("  Ingen åpne jobber.")
    else:
        for j in jobs:
            print(" ", format_job(j))


def menu_students_for_job():
    """Menypunkt 6: Vis studenter som matcher en jobb."""
    job_id = input_int("Jobb-ID: ")
    if job_id is None:
        print("Ugyldig tall. Prøv igjen.")
        return
    job = data.get_job_by_id(job_id)
    if job is None:
        print("Jobb ikke funnet.")
        return
    students = data.find_students_for_job(job_id)
    print(f"Studenter som matcher jobb {job_id} ({job.title}):")
    if not students:
        print("  Ingen studenter matcher.")
    else:
        for s in students:
            print(" ", format_student(s))


def menu_list_students():
    """Menypunkt 7: List alle studenter."""
    if not data.students:
        print("Ingen studenter registrert ennå.")
        return
    print("Alle studenter:")
    for s in data.students:
        print(" ", format_student(s))


def menu_list_companies():
    """Menypunkt 8: List alle bedrifter."""
    if not data.companies:
        print("Ingen bedrifter registrert ennå.")
        return
    print("Alle bedrifter:")
    for c in data.companies:
        print(" ", format_company(c))


def menu_list_jobs():
    """Menypunkt 9: List alle jobber."""
    if not data.jobs:
        print("Ingen jobber opprettet ennå.")
        return
    print("Alle jobber:")
    for j in data.jobs:
        print(" ", format_job(j))


def show_menu():
    """Skriv hovedmenyen."""
    print("\n--- Student-Work-Application ---")
    print("1. Registrer student")
    print("2. Registrer bedrift")
    print("3. Opprett jobb")
    print("4. Vis matchende jobber for en student")
    print("5. Vis åpne jobber sortert på budget")
    print("6. Vis studenter som matcher en jobb")
    print("7. List alle studenter")
    print("8. List alle bedrifter")
    print("9. List alle jobber")
    print("10. Fyll med demodata")
    print("0. Avslutt")


def main():
    """Hovedløkke: vis meny og utfør valg."""
    while True:
        show_menu()
        choice = input("Velg: ").strip()
        if choice == "0":
            print("Ha det bra!")
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
            print("Ugyldig valg. Velg 0–10.")


if __name__ == "__main__":
    main()
