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
    def save_user():
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
    top.geometry("300x250")
    top.config(bg="#f2f2f2")

    tk.Label(top, text="Add New User", font=("Arial", 14, "bold"), bg="#f2f2f2").pack(pady=10)

    tk.Label(top, text="Name", bg="#f2f2f2").pack()
    entry_name = tk.Entry(top, width=30)
    entry_name.pack(pady=5)

    tk.Label(top, text="City", bg="#f2f2f2").pack()
    entry_city = tk.Entry(top, width=30)
    entry_city.pack(pady=5)

    tk.Label(top, text="Emergency Contact", bg="#f2f2f2").pack()
    entry_contact = tk.Entry(top, width=30)
    entry_contact.pack(pady=5)

    tk.Button(top, text="Save", command=save_user, bg="green", fg="white").pack(pady=10)

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("🌸 Sakhi App")
root.geometry("350x400")
root.config(bg="#e6f2ff")

# Title
tk.Label(
    root,
    text="🌸 Sakhi Safety App",
    font=("Arial", 18, "bold"),
    bg="#e6f2ff",
    fg="#003366"
).pack(pady=20)

# Buttons
tk.Button(
    root,
    text="🚨 SOS ALERT",
    command=send_sos,
    bg="red",
    fg="white",
    font=("Arial", 12),
    width=20
).pack(pady=10)

tk.Button(
    root,
    text="👀 Find Nearby",
    command=find_nearby,
    bg="#4da6ff",
    fg="white",
    font=("Arial", 12),
    width=20
).pack(pady=10)

tk.Button(
    root,
    text="➕ Add User",
    command=add_user,
    bg="green",
    fg="white",
    font=("Arial", 12),
    width=20
).pack(pady=10)

tk.Button(
    root,
    text="Exit",
    command=root.quit,
    bg="black",
    fg="white",
    font=("Arial", 12),
    width=20
).pack(pady=20)

root.mainloop()