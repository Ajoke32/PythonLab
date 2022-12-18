from auto import user as u
from auto import privileges as p


priv = p.Privileges(['Allowed to add message','Allowed to ban message'])
admin = u.Admin("Anna","Naxe",priv,"anana.nxt@mail.com","Anet")

def test_preveligies_showing():
    assert admin.privileges.show_privileges()==['Allowed to add message','Allowed to ban message']

