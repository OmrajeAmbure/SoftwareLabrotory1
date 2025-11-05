from flask import Flask, request
import mysql.connector
from flask import render_template

app = Flask(__name__)

# Database Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Omraje@27",
    database="learnsql"
)
cursor = db.cursor()
@app.route("/",methods=["GET"])
def home():
    return render_template("index.html")
@app.route("/add_student", methods=["POST"])
def add_student():
    if request.method == "POST":
        roll_no = request.form['roll_no']
        name = request.form['name']
        marks = request.form['marks']
        email = request.form['email']
        sql_insert = "Insert into students (roll_no,name,marks,email) values (%s,%s,%s,%s)"
        cursor.execute(sql_insert,(roll_no,name,marks,email))
        db.commit()
        return render_template("index.html", message="Student added successfully"), 201
@app.route("/get_students", methods=["GET"])
def get_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    return render_template("students.html", students=students), 200
@app.route("/update_student/<int:roll_no>", methods=["GET", "POST"])
def update_student(roll_no):
    if request.method == "GET":
        cursor.execute("SELECT * FROM students WHERE roll_no=%s", (roll_no,))
        student = cursor.fetchone()
        return render_template("update_student.html", student=student)

    if request.method == "POST":
        name = request.form['name']
        marks = request.form['marks']
        email = request.form['email']

        sql_update = "UPDATE students SET name=%s, marks=%s, email=%s WHERE roll_no=%s"
        cursor.execute(sql_update, (name, marks, email, roll_no))
        db.commit()
        return render_template("index.html", message="Student updated successfully")
@app.route("/delete_student/<int:roll_no>", methods=["POST"])
def delete_student(roll_no):
    if request.method == "POST":
        sql_delete = "DELETE FROM students WHERE roll_no=%s"
        cursor.execute(sql_delete, (roll_no,))
        db.commit()
        return render_template("index.html", message="Student deleted successfully"), 200
if __name__ == "__main__":
    app.run(debug=True)
    
    