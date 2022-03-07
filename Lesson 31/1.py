class User:
    def __init__(self,first_name,last_name,age,place,date_of_registration,login_attempts=0):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.place=place
        self.date_of_registration=date_of_registration
        self.login_attempts=login_attempts
    def describe_user(self):
        print(f" Name:{self.first_name}\n Surname:{self.last_name}\n Age:{self.age}\n Place:{self.place}\n Date:{self.date_of_registration}")
    def greet_user(self):
        print(f"Hi,{self.first_name} {self.last_name}!")
    def increment_login_attempts(self):
        self.login_attempts+=1
        return self.login_attempts
    def reset_login_attempts(self):
        self.login_attempts=0
        return self.login_attempts
class  Admin ( User ):
    def __init__(self,first_name,last_name,age,place,date_of_registration,privileges):
        User.__init__(self,first_name,last_name,age,place,date_of_registration)
        self.privileges=privileges
    def  show_privileges ( self ):
        for  i  in  self . privileges :
            print(f"You can {i}")
u1=User("Yulia","Zinchenko",15,"Ukraine",2015)
u1.describe_user()
u1.greet_user()
u1.increment_login_attempts()
u1.increment_login_attempts()
u1.increment_login_attempts()
print(u1.login_attempts)
u1.reset_login_attempts()
print(u1.login_attempts)
a1=Admin("Yulia","Zinchenko",15,"Ukraine",2015,["Allowed to add","Allowed to delete users","Allowed to ban users"])
a1.show_privileges()
class Privileges:
    def __init__(self,privileges=a1.privileges):
        self.privileges=privileges
    def  show_privileges ( self ):
        Admin.show_privileges(self)
priv = Privileges ()
priv.show_privileges()
class  Admin ( User ):
    def __init__(self,first_name,last_name,age,place,date_of_registration,privileges=priv.privileges):
        User.__init__(self,first_name,last_name,age,place,date_of_registration)
        self.privileges=privileges
    def  show_privileges ( self ):
        for  i  in  self . privileges :
            print(f"You can {i}")
a2=Admin("Yulia","Zinchenko",15,"Ukraine",2015)
a2.show_privileges()
