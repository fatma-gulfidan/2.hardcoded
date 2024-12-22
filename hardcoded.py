# vulnerable_code.py

def login():
    username = "admin"
    password = "hardcodedpassword123"  # Hardcoded password (security vulnerability)

    entered_username = input("Enter your username: ")
    entered_password = input("Enter your password: ")

    if entered_username == username and entered_password == password:
        print("Login successful!")
    else:
        print("Login failed!")

if __name__ == "__main__":
    login()
