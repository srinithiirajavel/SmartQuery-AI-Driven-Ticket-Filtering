import json
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
import logging
import os

# Initialize FastAPI app
app = FastAPI()
security = HTTPBasic()

# File for storing feedback
FEEDBACK_FILE = "feedback_db.json"

# Mock user data
mock_users = {
    "user1": "password1",
    "user2": "password2"
}

# Sample ticket data
tickets_db = [
    [1, "Alice", "high", "Issue with login"],
    [2, "Bob", "medium", "Page loading slowly"],
    [3, "Alice", "low", "Error in report generation"],
    [4, "Bob", "high", "Security vulnerability in system"],
    [5, "Alice", "medium", "UI bug on settings page"]
]

# Setup logging
logging.basicConfig(level=logging.INFO)

# Model for query input and feedback
class Query(BaseModel):
    text: str

class Feedback(BaseModel):
    query: str
    feedback: str

# Authentication function
def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    if mock_users.get(credentials.username) != credentials.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return credentials.username

# Load feedback data from the JSON file
def load_feedback():
    if os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, "r") as f:
            return json.load(f)
    return []

# Save feedback data to the JSON file
def save_feedback(feedback_db):
    with open(FEEDBACK_FILE, "w") as f:
        json.dump(feedback_db, f, indent=4)

# Filter tickets based on query string (mocked logic)
def filter_tickets_by_query(query_text):
    filtered_tickets = []

    if "Alice" in query_text and "high" in query_text:
        filtered_tickets = [ticket for ticket in tickets_db if ticket[1] == "Alice" and ticket[2] == "high"]
    elif "Bob" in query_text and "medium" in query_text:
        filtered_tickets = [ticket for ticket in tickets_db if ticket[1] == "Bob" and ticket[2] == "medium"]
    elif "high" in query_text:
        filtered_tickets = [ticket for ticket in tickets_db if ticket[2] == "high"]
    elif "Alice" in query_text:
        filtered_tickets = [ticket for ticket in tickets_db if ticket[1] == "Alice"]
    else:
        filtered_tickets = tickets_db  # Default to all tickets

    return filtered_tickets

# Endpoint to verify credentials
@app.post("/login")
def login(credentials: HTTPBasicCredentials = Depends(security)):
    if mock_users.get(credentials.username) == credentials.password:
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")

# Endpoint to filter tickets based on a query
@app.post("/filter_tickets/")
def filter_tickets(query: Query, username: str = Depends(authenticate_user)):
    try:
        logging.info(f"User {username} requested query: {query.text}")
        tickets = filter_tickets_by_query(query.text)

        if not tickets:
            return {"tickets": [], "message": "No tickets found"}

        return {
            "tickets": tickets,
            "technical_filter": query.text  # SQL-like filter (in this case, the query string)
        }
    except Exception as e:
        logging.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while filtering tickets")

# Endpoint to submit feedback and store in the feedback_db.json
@app.post("/submit_feedback/")
def submit_feedback(feedback: Feedback, username: str = Depends(authenticate_user)):
    try:
        # Load existing feedback from file
        feedback_db = load_feedback()
        
        # Append new feedback
        feedback_db.append({"query": feedback.query, "feedback": feedback.feedback, "user": username})
        
        # Save feedback back to file
        save_feedback(feedback_db)

        logging.info(f"Feedback received from {username}: {feedback.feedback} for query: {feedback.query}")
        return {"message": "Feedback successfully received"}
    except Exception as e:
        logging.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while submitting feedback")

# Secure endpoint to demonstrate authentication
@app.get("/secure-endpoint")
def secure_endpoint(username: str = Depends(authenticate_user)):
    return {"message": f"Hello, {username}!"}
