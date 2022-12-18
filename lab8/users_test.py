from auto_users import user as u
from auto_admin import privileges as p
from auto_admin import admin as ad


user1=u.User("Petter","Dims","petter.dims@gmail.com","Piet")
user2=u.User("John","Tacks","john.Tacks@gmail.com","Piet",True)
user3=u.User("Mike","Fergin")
print(F"{user1.describe_user()}. {user1.greeting_user()}\n{user2.describe_user()}. {user2.greeting_user()}\n"
 F"{user3.describe_user()}. {user3.greeting_user()}")
for i in range(0,7):
    user3.increment_login_attempts()

print(user3.login_attempts)
user3.reset_login_attempts()
print(user3.login_attempts)

priv = p.Privileges(['Allowed to delete users','Allowed to add message'])
admin1=ad.Admin("a","a",priv)
print(admin1.privileges.show_privileges())