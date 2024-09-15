from pydantic import BaseModel
from fastapi import FastAPI
import sqlite3

app = FastAPI()

# Feedback model to collect user feedback on query results
class Feedback(BaseModel):
    query: str
    result: str
    feedback: str

# Function to store feedback into a database
def store_feedback(query, result, feedback):
    conn = sqlite3.connect('feedback.db')  # Create or connect to feedback.db
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS feedback 
                      (query TEXT, result TEXT, feedback TEXT)''')
    cursor.execute('INSERT INTO feedback (query, result, feedback) VALUES (?, ?, ?)', (query, result, feedback))
    conn.commit()
    conn.close()

# Endpoint to submit feedback
@app.post("/submit_feedback/")
async def submit_feedback(feedback: Feedback):
    store_feedback(feedback.query, feedback.result, feedback.feedback)
    return {"status": "Feedback recorded"}
