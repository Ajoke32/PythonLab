from auto_users import user as u


class Admin(u.User):
    def __init__(self, first_name, last_name,privileges,email="not set",nick="not set", is_apply=False,login_attempts=0):
        super().__init__(first_name, last_name,email,nick,is_apply,login_attempts) #передача в базовий клас полів
        self.privileges=privileges #додатковий атрибут для привілегій







