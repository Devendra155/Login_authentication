import json
import os
import getpass

USERS_FILE = "users.json"
SESSION_FILE = "session.txt"


def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, 'r') as f:
        return json.load(f)


def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f)


def register():
    users = load_users()
    username = input("Choose a username: ")
    if username in users:
        print("Username already exists. Try another one.")
        return
    password = getpass.getpass("Choose a password: ")
    users[username] = password
    save_users(users)
    print("Registration successful!")


def login():
    users = load_users()
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    if users.get(username) == password:
        with open(SESSION_FILE, 'w') as f:
            f.write(username)
        print("Login successful!")
    else:
        print("Invalid credentials!")


def logout():
    if os.path.exists(SESSION_FILE):
        os.remove(SESSION_FILE)
        print("Logged out.")
    else:
        print("You are not logged in.")


def secured_page():
    if not os.path.exists(SESSION_FILE):
        print("Access denied. Please log in first.")
        return
    with open(SESSION_FILE, 'r') as f:
        username = f.read()
    print(f"Welcome to the secured page, {username}!")


def main():
    while True:
        print("\n=== Authentication System ===")
        print("1. Register")
        print("2. Login")
        print("3. Secured Page")
        print("4. Logout")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            secured_page()
        elif choice == '4':
            logout()
        elif choice == '5':
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
