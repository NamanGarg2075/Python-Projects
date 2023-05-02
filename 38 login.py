
all_users = []

sign_options = input("For login type (L)\
                     For register type (R): ")



class UserDetails:
    def __init__(self,name,username,password,hint="0"):
        self.name = name
        self.username = username
        self.password = password
        self.hint = hint
        # all_name.append(self.name)
        all_users.append(self.username)
        # all_pass.append(self.password)

class Login():
    def __init__(self):
        print("YO")

class Register:
    def __init__(self):
        self.name = input("NAME")
        self.username = input("username")
        self.password = input("password")


if sign_options.lower() == "l":
    Login()
elif sign_options.lower() == "r":
    Register()
else:
    print("USER NOT FOUND!!!")
