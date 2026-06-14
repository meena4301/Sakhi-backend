import json

# ---------------- LOAD USERS ----------------
def load_users():
    global users
    try:
        with open("users.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        print("No previous data found, starting fresh.")


    
