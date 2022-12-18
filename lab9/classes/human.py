class Human:
    default_name="default"
    default_age="not set"

    def __init__(self,name, age,__money,__house):
        self.name=name
        self.age=age
        self.__money=__money
        self.__house=__house

    def info(self):
        return F"Name:{self.name}\nAge:{self.age}\nHouse:{self.__house}\nMoney:{self.__money}"

    @classmethod
    def default_info(cls):
        return F"{cls.default_name} {cls.default_age}"

    def  make_deal(self,money,house):
        self.__money-=money
        self.__house=house

    def earn_money(self,money):
        self.__money+=money

    def buy_house(self,house,discount=10):
        if self.__money>=house._price:
            self.__money-=house.final_price(discount)
            return "House bought"
        else:
            return "not enough money"


class House:
    def __init__(self,_area,_price):
        self._area=_area
        self._price=_price

    def final_price(self,discount):
        return self._price-self._price*discount/100

class SmallHouse(House):
    def __init__(self,_price):
        self._area = "40m2"
        super().__init__(self._area, _price)
