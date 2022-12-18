from classes import coin as c
from classes import bank as b
from classes import car as m
from classes import dog as d
from classes import pets as p
from classes import buffer as buff
from classes import exception_ex as ex
from classes import roman as r
from online_shop import shop


dog2 = d.AmericanBuldog("adog",2)
dog3 = d.BelgainSheepDog("bels",18)

user = b.Bank(200)
user.put(-200)
user.get_balance()
user.withdraw(100)
user.get_balance()
user.withdraw(500)
user.get_balance()


coin_m = c.Coin('heads')

for i in range (1,10):
    coin_m.toos()


car_ex = m.Car("mark1","model1",2003)

for x in range(0,5):
    car_ex.accelerate()
    print(F"+speed: {car_ex.get_speed()}")

for x in range(0,5):
    car_ex.brake()
    print(F"-speed: {car_ex.get_speed()}")


pets_l = p.Pets()
dog1=d.Dog("dofea",12)
pets_l.add_pet(dog1)
dog2 =d.AmericanBuldog("anesc",2)
pets_l.add_pet(dog2)
dog3 = d.BelgainSheepDog("belgax",13)
pets_l.add_pet(dog3)

for x in pets_l.pets_list:
    print(F"{x.get_info()},{x.nature}")


buffer_k = buff.Buffer()
buffer_k.add(1,2,3)
print(buffer_k.get_current_part())
buffer_k.add(4)
print(buffer_k.get_current_part())
buffer_k.add(5)
print(buffer_k.get_current_part())
buffer_k.add(2,4,4,2,3,4,5,4,2)
print(buffer_k.get_current_part())
buffer_k.add(7)
print(buffer_k.get_current_part())

a = input("Enter you name:")
if len(a)<10:
    raise ex.ExceptionEx


to = r.RomanToIneger("MMMDCCXXIV")
print(to.to_int())
a = r.IntToRoman(15)
print(a.printRoman())


store = shop.Shop("Gucci","Clothes")
print(F"{store.store_type} {store.shop_name}")
print(store.open_shop())
print(store.describe_shop())

store2=shop.Shop("Lui","Wallets")
print(store2.describe_shop())

store3=shop.Shop("Intel","Tech")
print(store3.describe_shop())
print(store3.number_of_units)
store3.number_of_units=5
print(store3.number_of_units)

store2.set_number_of_units(3)
print(store2.number_of_units)
store2.increment_number_of_units(4)
print(store2.number_of_units)


store_discount = shop.Discount(["tie","clothes","book"],"Darpsx","typesx")
print(store_discount.discount_products)

