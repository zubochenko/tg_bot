from utils import is_user_exists, is_login_correct, is_user_admin, save_user

class User:
    def __init__(self, login, password, mode='user'):
        self.login = login
        self.password = password
        self.mode = mode

    def __str__(self):
        return f"login: {self.login}, password: {self.password}, mode: {self.mode}"


admin = User('admin', "admin_pass", 'admin')
save_user('admin', "admin_pass")
users = [admin]

while True:
    command = input("Enter command: ")
    if command == "login":
        login = input("Enter login: ")
        password = input("Enter password: ")
        if not is_user_exists(login, users):
            print("User was not found!")
        elif not is_login_correct(login, password, users):
            print("Incorrect login or password!")
        else:
            print("Welcome!")
    elif command == "register":
        login = input("Enter login: ")
        if is_user_exists(login, users):
            print("Sorry, user is already exists!")
        else:
            password = input("Enter password: ")
            new_user = User(login, password)
            users.append(new_user)
            save_user(login, password)
            print("User was created")
    elif command == "all_users":
        login = input("Enter login: ")
        password = input("Enter password: ")
        if is_user_admin(login, password, users):
            for user in users:
                print(user)
        else:
            print("Access Denied!")