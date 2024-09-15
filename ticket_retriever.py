import sqlite3
from typing import List

def get_tickets(filter_query: str) -> List[dict]:
    try:
        conn = sqlite3.connect('data/new_mock_tickets.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tickets WHERE {}".format(filter_query))
        tickets = cursor.fetchall()
        conn.close()
        return tickets
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []
