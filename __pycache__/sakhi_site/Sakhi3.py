users = {
    "Meena": {
        "city": "Vijayawada",
        "emergency_contact": "Harshini"
    },
    "Harshini": {
        "city": "Guntur",
        "emergency_contact": "Meena"
    },
    "Ravi": {
        "city": "Vijayawada",
        "emergency_contact": "None"
    }
}

def send_sos(user):
    print("\n🚨 SOS ALERT from", user)
    print("📍 Location:", users[user]["city"])
    print("📞 Emergency contact:", users[user]["emergency_contact"])

def find_nearby(user):
    print("\n👀 Checking nearby users for", user)

    for name, data in users.items():
        if name != user and data["city"] == users[user]["city"]:
            print("📍 Nearby:", name)

# ➕ NEW USER REGISTER FUNCTION
def add_user():
    name = input("Enter new name: ").title()
    city = input("Enter city: ").title()
    contact = input("Enter emergency contact: ").title()

    users[name] = {
        "city": city,
        "emergency_contact": contact
    }

    print("✅ User added successfully!")

# 🔐 LOGIN
current_user = input("Enter your name: ").title()

if current_user not in users:
    print("User not found 😅")
else:
    while True:
        print("\n🌸 Sakhi App Menu")
        print("1. Send SOS 🚨")
        print("2. Find Nearby 👀")
        print("3. Exit ❌")
        print("4. Add New User ➕")

        choice = input("Enter choice: ")

        if choice == "1":
            send_sos(current_user)
        elif choice == "2":
            find_nearby(current_user)
        elif choice == "3":
            print("Bye 👋 Stay safe!")
            break
        elif choice == "4":
            add_user()
        else:
            print("Invalid choice 😅 Try again")