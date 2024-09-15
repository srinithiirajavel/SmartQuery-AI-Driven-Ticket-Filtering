# backend/nlu_module.py

import spacy
from typing import Dict, Any

# Load the small English language model
nlp = spacy.load("en_core_web_sm")

# backend/nlu_module.py
def parse_query(query_text: str) -> dict:
    print("Parsing query:", query_text)
    
    # Sample simple logic to parse "assigned Alice priority high"
    words = query_text.split()
    parsed_query = {
        "attributes": [],
        "values": []
    }
    
    # Find 'assigned' and 'priority' and capture their values
    if "assigned" in words:
        assigned_index = words.index("assigned")
        parsed_query["attributes"].append("assigned")
        parsed_query["values"].append(words[assigned_index + 1])
    
    if "priority" in words:
        priority_index = words.index("priority")
        parsed_query["attributes"].append("priority")
        parsed_query["values"].append(words[priority_index + 1])
    
    print("Parsed query result:", parsed_query)
    return parsed_query
