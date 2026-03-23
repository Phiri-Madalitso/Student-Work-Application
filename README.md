# Student-Work-Application

An application where students and companies can collaborate through job postings and skill matching.

## How to run

1. Open a terminal in this folder.
2. Run:

```bash
python Main.py
```

## What the application does

- Register students with ID, name, email, and skills
- Register companies with ID, name, and email
- Create jobs connected to a company
- Find matching open jobs for a student
- Find matching students for a job
- Sort jobs by budget

## Data structures used

The app uses both lists and dictionaries in `data.py`:

- Lists: store all students, companies, and jobs for iteration/filtering/sorting
- Dicts (`*_by_id`): provide fast ID lookup

## Time complexity (important functions)

- `get_student_by_id`, `get_company_by_id`, `get_job_by_id`: **O(1)** average-case dictionary lookup
- `find_matching_jobs_for_student`: **O(n)** over number of jobs
- `find_students_for_job`: **O(n)** over number of students
- `get_jobs_sorted_by_budget`: **O(n log n)** for sorting (plus optional O(n) filtering)

## Project structure

- `Main.py`: menu and user interaction
- `data.py`: central data layer and business logic
- `Model/Student.py`: `Student` class
- `Model/Company.py`: `Company` class
- `Model/Jobs.py`: `Job` class
