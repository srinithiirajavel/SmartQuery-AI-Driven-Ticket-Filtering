import json

def load_feedback():
    try:
        with open("feedback.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_feedback(feedback):
    with open("feedback.json", "w") as f:
        json.dump(feedback, f, indent=4)
