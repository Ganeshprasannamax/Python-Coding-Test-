# Welcome to Login Page Api 
# Here you can login through Your Login credentials

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Login:
    def __init__(self):
        self.users = []

    def add_user(self, username, password):
        user = User(username, password)
        self.users.append(user)

    def validate_user(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return True
        return False

login = Login()
login.add_user('Ganesh', 'password@123')
login.add_user('Stevewaugh', 'passw0rd!')
# Loign Page 
class UserSession:
    def __init__(self):
        self.username = None
        self.logged_in = False

    def login(self):
        username = input("Username: ")
        password = input("Password: ")
        if self.validate_input(username, password):
            if login.validate_user(username, password):
                self.username = username
                self.logged_in = True
                print("Login successful!")
            else:
                print("Invalid credentials. Login failed.")
        else:
            print("Invalid input. Login failed.")
# If user Wants to Logout 
    def logout(self):
        self.username = None
        self.logged_in = False
        print("Logout successful!")

    def validate_input(self, username, password):
        # Check if username and password are not empty
        if not username or not password:
            return False
        # Check if username and password are alphanumeric
        if not username.isalnum() or not password.isalnum():
            return False
        # Check if username and password meet a minimum length requirement
        if len(username) < 3 or len(password) < 6:
            return False
        return True
# Prompts for username and password input
user_session = UserSession()
user_session.login() 
user_session.logout()








