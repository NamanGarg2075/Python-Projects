
all_users = []
all_name = []
all_pass = []

obj = [all_name,all_users,all_pass]

class UserDetails:
    def __init__(self,name,username,password,hint="0"):
        self.name = name
        self.username = username
        self.password = password
        self.hint = hint
        all_name.append(self.name)
        all_users.append(self.username)
        all_pass.append(self.password)
        print("Created")

class Login():
    pass

class Register():
    pass

for i in range(1,3):
    obj_name = input("name of object")
    obj_username = input("username of object")
    obj_pass = input("password of object")

    object = UserDetails(obj_name,obj_pass,obj_username)


for i in obj:
    print(i)