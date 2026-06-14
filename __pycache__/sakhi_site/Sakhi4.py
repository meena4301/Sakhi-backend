import tkinter as tk
from tkinter import messagebox

# ---------------- DATA ----------------
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

current_user = "Meena"

# ---------------- FUNCTIONS ----------------
def send_sos():
    msg = f"🚨 SOS ALERT from {current_user}\n"
    msg += f"📍 Location: {users[current_user]['city']}\n"
    msg += f"📞 Emergency: {users[current_user]['emergency_contact']}"
    messagebox.showwarning("SOS ALERT", msg)

def find_nearby():
    result = ""

    for name, data in users.items():
        if name != current_user and data["city"] == users[current_user]["city"]:
            result += f"📍 {name} is nearby\n"

    if result == "":
        result = "No nearby users found 😅"

    messagebox.showinfo("Nearby Users", result)

def add_user():
    def save_new():
        name = entry_name.get().title()
        city = entry_city.get().title()
        contact = entry_contact.get().title()

        users[name] = {
            "city": city,
            "emergency_contact": contact
        }

        messagebox.showinfo("Success", "User Added Successfully!")
        top.destroy()

    top = tk.Toplevel()
    top.title("Add User")

    tk.Label(top, text="Name").pack()
    entry_name = tk.Entry(top)
    entry_name.pack()

    tk.Label(top, text="City").pack()
    entry_city = tk.Entry(top)
    entry_city.pack()

    tk.Label(top, text="Emergency Contact").pack()
    entry_contact = tk.Entry(top)
    entry_contact.pack()

    tk.Button(top, text="Save", command=save_new).pack()

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("🌸 Sakhi App")
root.geometry("300x300")

tk.Label(root, text="Sakhi Safety App", font=("Arial", 16)).pack(pady=10)

tk.Button(root, text="🚨 SOS", command=send_sos, bg="red", fg="white").pack(pady=10)
tk.Button(root, text="👀 Find Nearby", command=find_nearby).pack(pady=10)
tk.Button(root, text="➕ Add User", command=add_user).pack(pady=10)

tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

root.mainloop()