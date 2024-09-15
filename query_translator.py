from typing import Dict, Any

# backend/query_translator.py
def translate_query(parsed_query: dict) -> str:
    print("Parsed query for translation:", parsed_query)
    
    filters = []
    if "attributes" in parsed_query:
        attributes = parsed_query["attributes"]
        
        # Generate SQL based on attributes
        if "assigned" in attributes:
            assignee_value = parsed_query["values"][attributes.index("assigned")]
            filters.append("assignee = '{}'".format(assignee_value))
        
        if "priority" in attributes:
            priority_value = parsed_query["values"][attributes.index("priority")]
            filters.append("priority = '{}'".format(priority_value))
    
    # Combine filters into a SQL query
    query = " AND ".join(filters)
    print("Generated SQL query:", query)
    return query

