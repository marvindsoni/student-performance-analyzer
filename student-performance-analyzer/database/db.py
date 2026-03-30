mport sqlite3

DATABASE_NAME = "student_database.db"


# Connect to database
def connect_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


# Create tables using schema.sql
def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    with open("schema.sql", "r") as file:
        sql_script = file.read()

    cursor.executescript(sql_script)

    conn.commit()
    conn.close()


# Add new user
def add_user(username, password):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        (username, password)
    )

    conn.commit()
    conn.close()


# Add student marks
def add_student(student_name, subject, marks):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (student_name, subject, marks) VALUES (?, ?, ?)",
        (student_name, subject, marks)
    )

    conn.commit()
    conn.close()


# View all students
def get_students():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    conn.close()

    return students


# Run this file to create tables
if __name__ == "__main__":
    create_tables()
    print("Database and tables created successfully.")