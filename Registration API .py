# Registration Api 
# This Class for New Sign-up Users 
import re
class User:
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

class Registration:
    def __init__(self):
        self.users = []

    def add_user(self, first_name, last_name, email, password):
        user = User(first_name, last_name, email, password)
        self.users.append(user)

# Basic validation 
    def validate_email(self, email):
        if "@" in email and "." in email:
            return True
        return False
    def validate_password(self):
        if len(self.password) >= 6 and re.search('[^a-zA-Z0-9]', self.password):
            return True
        return False

registration = Registration()
registration.add_user('Ganesh', 'Prasanna', 'Ganeshprasanna@example.com', 'Password@123')
registration.add_user('Steve', 'waugh', 'stevewaugh@example.com', 'passw0rd!')

class UserSession:
    def __init__(self):
        self.username = None
        self.logged_in = False

    def register(self):
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        email = input("Email: ")
        password = input("Password: ")
        if self.validate_input(first_name, last_name, email, password):
            if registration.validate_email(email) and registration.validate_password(password):
                registration.add_user(first_name, last_name, email, password)
                print("Registration successfull! Enjoy Shopping With Us!")
            else:
                print("Invalid email or password. Registration failed Try Again.")
        else:
            print("Invalid input. Registration failed Try Again with valid details.")
# After Sign-up Login with the credentials
    def validate_input(self, first_name, last_name, email, password):
        # Checking if all fields are not empty
        if not first_name or not last_name or not email or not password:
            return False
        # Checking if email is valid
        if not registration.validate_email(email):
            return False
        # Checking if password is valid
        if not registration.validate_password(password):
            return False
        return True
# Prompts for first name, last name, email, and password input
user_session = UserSession()
user_session.register()

# If you successFully Registrated  You will Redirect to Login Page Api!

