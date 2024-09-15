import sqlite3

def check_db():
    conn = sqlite3.connect('data/new_mock_tickets.db')
    cursor = conn.cursor()

    # Check tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables:", [table[0] for table in tables])

    # Check data in 'tickets' table
    cursor.execute("SELECT * FROM tickets;")
    rows = cursor.fetchall()
    print("Data in tickets table:", rows)

    conn.close()

if __name__ == "__main__":
    check_db()
