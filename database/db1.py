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
con.commit()
print("Table created successfully")

# INSERT function
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
    except Exception as e:
        print("Insert failed:", e)

# UPDATE function
def update_data(USN, ADDRESS):
    try:
        cursor.execute("UPDATE Student SET ADDRESS = ? WHERE USN = ?", (ADDRESS, USN))
        con.commit()
        if cursor.rowcount == 0:
            print(f"No record found with USN '{USN}' to update.")
        else:
            print("Data updated!")
    except Exception as e:
        print("Update failed:", e)

# DELETE function
def delete_data(USN):
    try:
        cursor.execute("DELETE FROM Student WHERE USN = ?", (USN,))
        con.commit()
        if cursor.rowcount == 0:
            print(f"No record found with USN '{USN}' to delete.")
        else:
            print("Data deleted!")
    except Exception as e:
        print("Delete failed:", e)

# VIEW function
def view_data():
    try:
        cursor.execute("SELECT * FROM Student")
        rows = cursor.fetchall()
        if not rows:
            print("No records found.")
        for row in rows:
            print(row)
    except Exception as e:
        print("View failed:", e)

# --- Example usage ---
add_val("John", "1a", 4, "2001-07-12", "MCA", "Mumbai")
view_data()
update_data("1a", "Kerala")
view_data()
delete_data("1a")
view_data()

# Close connection when done
con.close()