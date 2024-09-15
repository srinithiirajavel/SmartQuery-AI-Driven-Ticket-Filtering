PREREQUISITES :
Before executing the project, ensure that the following are installed:
1.Python 3.8+
2.pip (Python package manager)
3.FastAPI (Swagger/ Curl)
4.Uvicorn (ASGI server for FastAPI)
5.Streamlit
6.SQLite3 (Database for storing tickets)

REPOSITORY :
1.Git Clone - https://github.com/srinithiirajavel/SmartQuery-AI-Driven-Ticket-Filtering
 
2.Setting up Environment - python -m venv venv
                           venv\Scripts\activate

3.Install Dependencies - pip install -r requirements.txt

4.Database Setup - python create_db.py


RUNNING THE APPLICATION :
1.FastAPI backend service (Start the Backend (FastAPI)) - uvicorn backend.main:app --host 0.0.0.0 --port 8000

2.Run the Frontend Application (Start the Frontend (Streamlit)) - streamlit run frontend/app.py

USER AUTHENTICATION
user1: password1
user2: password2

License
This project is licensed under the MIT License. See the LICENSE file for details.


PPROJECT STRUCTURE :

nl_ticket_filter/
├── backend/
│   ├── main.py                # FastAPI backend entry point
│   ├── nlu_module.py          # Module for natural language understanding of queries
│   ├── query_translator.py    # Translates parsed queries to SQL
│   ├── ticket_retriever.py    # Retrieves tickets from the database
│   └── utils.py               # Utility functions (helper methods, logging, etc.)
├── frontend/
│   └── app.py                 # Streamlit frontend application
├── data/
│   └── tickets.db             # SQLite database for storing ticket data
├── tests/
│   ├── test_nlu.py            # Unit tests for the NLU module
│   ├── test_query_translation.py # Unit tests for query translation
│   └── test_ticket_retrieval.py  # Unit tests for ticket retrieval
├── requirements.txt           # List of project dependencies
└── README.md                  # Detailed instructions on setup and usage


Your Name: SRINITHI RAJAVEL
Project Repository: SmartQuery-AI-Driven-Ticket-Filtering
 





