import sqlite3

def create_db():
    conn = sqlite3.connect('data/new_mock_tickets.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            assignee TEXT,
            priority TEXT,
            description TEXT
        )
    ''')

    cursor.execute("INSERT INTO tickets (assignee, priority, description) VALUES ('Alice', 'high', 'Fix bug in login')")
    cursor.execute("INSERT INTO tickets (assignee, priority, description) VALUES ('Bob', 'medium', 'Update user profile page')")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_db()
