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


# 🔐 LOGIN SYSTEM
current_user = input("Enter your name: ")

if current_user not in users:
    print("User not found 😅")
else:
    while True:
        print("\n🌸 Sakhi App Menu")
        print("1. Send SOS 🚨")
        print("2. Find Nearby 👀")
        print("3. Exit ❌")

        choice = input("Enter choice: ")

        if choice == "1":
            send_sos(current_user)
        elif choice == "2":
            find_nearby(current_user)
        elif choice == "3":
            print("Bye 👋 Stay safe!")
            break
        else:
            print("Invalid choice 😅 Try again")