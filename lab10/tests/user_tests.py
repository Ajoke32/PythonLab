from auto import user as u

user = u.User("Jonh","Timber","jon.timber@mail.com","Bisider")

def test_decribe_user():
    assert user.describe_user()=="You name: Jonh"

def test_greeteng():
    assert user.greeting_user()=="Welcome, Jonh Timber"

def test_increment_attempts():
    user.increment_login_attempts()
    assert user.login_attempts==1

def test_reset_attempts():
    user.reset_login_attempts()
    assert user.login_attempts==0