# CRUD_System_PUCPR
This is a basic computer program to manage a school, made with Python. It runs in the terminal and doesn't have fancy buttons or windows.

With it, you can:
*   Add, view, change, and delete information for **Students**.
*   Add, view, change, and delete information for **Courses** (subjects).
*   Add, view, change, and delete information for **Teachers**.
*   Create, view, change, and delete **Classes** (linking a course with a teacher).
*   Make, view, change (only the date), and delete **Enrollments** (putting a student in a class).

All data is saved in `.json` files (which are like organized text files) so you don't lose anything when you close the program.

## What can you do with it?

### Students
*   Register a new student (name, student ID, and a unique personal ID). The program checks if the student ID or personal ID already exists.
*   See a list of all students.
*   Delete a student from the list.
*   Change a student's name, student ID, or personal ID.

### Courses
*   Register a new course (name, start date, end date, hours).
*   See a list of all courses.
*   Delete a course.
*   Change course details.

### Teachers
*   Register a new teacher (name, teacher ID, and a unique personal ID). The program checks if the teacher ID or personal ID already exists.
*   See a list of all teachers.
*   Delete a teacher.
*   Change teacher details.

### Classes
*   Create a new class (with a code, an existing course, and an existing teacher).
*   See a list of all classes.
*   Delete a class.
*   Change a class's code, course, or teacher.

### Enrollments
*   Enroll a student in a class (with a date). The program checks if the student is already in that class.
*   See a list of all enrollments.
*   Delete an enrollment.
*   Change the date of an enrollment.

## What was used to make it?

*   **Python 3:** The programming language.
*   **`json` module:** To read and write the data files.
*   **`os` and `sys` modules:** For things like clearing the terminal screen.

## Example of how data is stored

Data is kept in files like `arquivo_estudante.json`. Inside them, it looks something like this:

```json
[
  {
    "nome": "Maria Souza",
    "ra": 123,
    "cpf": "11122233300"
  },
  {
    "nome": "Joao Silva",
    "ra": 456,
    "cpf": "44455566600"
  }
]
