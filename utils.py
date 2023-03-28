def is_user_exists(login, users):
    for user in users:
        if user.login == login:
            return True
    return False

def is_login_correct(login, password, users):
    for user in users:
        if user.login == login and user.password == password:
            return True
    return False

def is_user_admin(login, password, users):
    for user in users:
        if user.login == login and user.password == password and user.mode == "admin":
            return True
    return False

def save_user(login, password):
    with open("users.txt", 'a') as f:
        f.write(login + " " + password+ " \n")

def read_users():
    with open("users.txt", 'r') as f:
        lines = f.readlines()
        for line in lines:
            splitted_line = line.split()
            login, password = splitted_line[0], splitted_line[1]
            return login, password

print(hash('password') == hash("password"))