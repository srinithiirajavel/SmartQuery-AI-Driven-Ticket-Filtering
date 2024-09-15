import streamlit as st
import requests
from requests.auth import HTTPBasicAuth

# Backend URL
BACKEND_URL = "http://localhost:8000"

# Function to authenticate user with backend
def authenticate(username, password):
    response = requests.post(
        f"{BACKEND_URL}/login",
        auth=HTTPBasicAuth(username, password)
    )
    return response.status_code == 200

# Function to filter tickets from the backend
def filter_tickets(query):
    response = requests.post(
        f"{BACKEND_URL}/filter_tickets/",
        json={"text": query},
        auth=HTTPBasicAuth(st.session_state["username"], st.session_state["password"])
    )
    return response.json() if response.status_code == 200 else None

# Function to submit feedback
def submit_feedback(query, feedback):
    response = requests.post(
        f"{BACKEND_URL}/submit_feedback/",
        json={"query": query, "feedback": feedback},
        auth=HTTPBasicAuth(st.session_state["username"], st.session_state["password"])
    )
    return response.json() if response.status_code == 200 else None

# Main app
def main():
    st.title("Ticket Filter")

    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if not st.session_state["logged_in"]:
        st.header("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if authenticate(username, password):
                st.session_state["logged_in"] = True
                st.session_state["username"] = username
                st.session_state["password"] = password
                st.success("Login successful")
            else:
                st.error("Invalid credentials")
    
    if st.session_state["logged_in"]:
        st.header("Select a query")

        queries = {
            "assigned Alice priority high": {
                "description": "Show tickets assigned to Alice with high priority.",
                "query": "assigned Alice priority high"
            },
            "assigned Bob priority medium": {
                "description": "Show tickets assigned to Bob with medium priority.",
                "query": "assigned Bob priority medium"
            },
            "priority high": {
                "description": "Show all high priority tickets.",
                "query": "priority high"
            },
            "assigned Alice": {
                "description": "Show all tickets assigned to Alice.",
                "query": "assigned Alice"
            }
        }

        selected_query = st.selectbox(
            "Select a query",
            options=list(queries.keys()),
            format_func=lambda query: queries[query]["description"]
        )

        st.subheader("Query Interpretation:")
        st.write(f"Selected Query: {selected_query}")
        st.write(f"Description: {queries[selected_query]['description']}")

        refined_query = st.text_area(
            "You can manually adjust the query interpretation here:",
            value=queries[selected_query]['query']
        )

        if st.button("Submit Refined Query"):
            tickets_response = filter_tickets(refined_query)
            if tickets_response and "tickets" in tickets_response:
                st.subheader("Filtered Tickets:")
                tickets = tickets_response["tickets"]
                if tickets:
                    st.table(tickets)
                else:
                    st.warning("No tickets found")

        feedback_text = st.text_area("Provide feedback on the query:")
        if st.button("Submit Feedback"):
            feedback_response = submit_feedback(refined_query, feedback_text)
            if feedback_response:
                st.success(feedback_response.get("message", "Feedback submitted successfully"))
            else:
                st.error("Error submitting feedback")

        if st.button("Logout"):
            st.session_state["logged_in"] = False
            st.session_state["username"] = ""
            st.session_state["password"] = ""
            st.experimental_rerun()

if __name__ == "__main__":
    main()
