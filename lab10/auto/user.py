class User:
    def __init__(self,first_name,last_name,email="not set",nick="not set", is_apply=False,login_attempts=0):
        self.fist_name = first_name
        self.last_name=last_name
        self.email = email  #ініціалізація атрибутів
        self.nick =nick
        self.is_apply=is_apply
        self.login_attempts=login_attempts

    def describe_user(self):
        return F"You name: {self.fist_name}" #імя користувача

    def greeting_user(self):
        return F"Welcome, {self.fist_name} {self.last_name}" #вітання користувача

    def increment_login_attempts(self):
        self.login_attempts+=1   #інкрементація спроб
    def reset_login_attempts(self):
        self.login_attempts=0 #онулення спроб


class Admin(User):
    def __init__(self, first_name, last_name,privileges,email="not set",nick="not set", is_apply=False,login_attempts=0):
        super().__init__(first_name, last_name,email,nick,is_apply,login_attempts) #передача в базовий клас полів
        self.privileges=privileges #додатковий атрибут для привілегій