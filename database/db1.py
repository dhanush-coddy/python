import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
con = sqlite3.connect("student.db")
cursor = con.cursor()

# Create the Student table if it does not already exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS Student(
    NAME TEXT,
    USN TEXT PRIMARY KEY,
    SEM INTEGER,
    DOB TEXT,
    DEPT TEXT,
    ADDRESS TEXT)
""")

# Commit the transaction
con.commit()

print("Table created successfully")
def add_val(NAME, USN, SEM, DOB, DEPT, ADDRESS):
    try:
        cursor.execute(
            "INSERT INTO Student(NAME, USN, SEM, DOB, DEPT, ADDRESS) VALUES (?, ?, ?, ?, ?, ?)",
            (NAME, USN, SEM, DOB, DEPT, ADDRESS)
        )
        con.commit()
        print("Record added!")
    except sqlite3.IntegrityError:
        print("Error: Record with this USN already exists.")
        
add_val("abc", "4a", 2, "23-05-2025", "MCA", "Manglore")

def view_data():
    cursor.execute("SELECT * FROM Student")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


view_data()
