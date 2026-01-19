from flask import Flask, render_template, request, redirect
import sqlite3
from database import connect_db

app = Flask(__name__)

# Ensure database + table
connect_db()

def get_connection():
    return sqlite3.connect("students.db")

@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_connection()
    cur = conn.cursor()

    if request.method == "POST":
        roll = request.form["roll"]
        name = request.form["name"]
        course = request.form["course"]

        try:
            cur.execute(
                "INSERT INTO students (roll, name, course) VALUES (?, ?, ?)",
                (roll, name, course)
            )
            conn.commit()
        except:
            pass   # duplicate roll avoid

    cur.execute("SELECT * FROM students")
    students = cur.fetchall()
    conn.close()

    return render_template("index.html", students=students)

@app.route("/delete/<int:roll>")
def delete_student(roll):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE roll=?", (roll,))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_connection()
    cur = conn.cursor()

    last_added_roll = None

    if request.method == "POST":
        roll = request.form["roll"]
        name = request.form["name"]
        course = request.form["course"]

        try:
            cur.execute(
                "INSERT INTO students (roll, name, course) VALUES (?, ?, ?)",
                (roll, name, course)
            )
            conn.commit()
            last_added_roll = roll
        except:
            pass

    cur.execute("SELECT * FROM students")
    students = cur.fetchall()
    conn.close()

    return render_template(
        "index.html",
        students=students,
        last_added_roll=last_added_roll
    )
