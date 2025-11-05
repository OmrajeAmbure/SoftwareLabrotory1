import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",          # your MySQL username
    password="Sahilkapse10#",          # your MySQL password
    database="student_db" # your database name
)

cursor = conn.cursor()

# --- Functions for operations ---

def add_student():
    name = input("Enter name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")
    cursor.execute("INSERT INTO students (name, age, course) VALUES (%s, %s, %s)", (name, age, course))
    conn.commit()
    print("Student added successfully!\n")

def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    print("\n--- Student Records ---")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Course: {row[3]}")
    print()

def edit_student():
    student_id = input("Enter student ID to edit: ")
    name = input("Enter new name: ")
    age = input("Enter new age: ")
    course = input("Enter new course: ")
    cursor.execute("UPDATE students SET name=%s, age=%s, course=%s WHERE id=%s",
                   (name, age, course, student_id))
    conn.commit()
    print("Student record updated!\n")

def delete_student():
    student_id = input("Enter student ID to delete: ")
    cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))
    conn.commit()
    print("Student deleted!\n")

# --- Main Menu ---
while True:
    print("===== STUDENT DATABASE MENU =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Edit Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        edit_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.\n")

# Close the connection
cursor.close()
conn.close()