class Shop:
    def __init__(self,name, s_type,number_of_units=0):
        self.shop_name=name
        self.store_type=s_type
        self.number_of_units=number_of_units

    def describe_shop(self):
        return F"{self.shop_name} {self.store_type}"

    @staticmethod
    def open_shop():
        return F"Shop open"

    def set_number_of_units(self, amount):
        if amount>0:
            self.number_of_units=amount
            return F"units was be added!"
        else:
            return F"invalid value!"

    def increment_number_of_units(self, anount):
        if anount>self.number_of_units:
            self.number_of_units+=anount
            return True
        else:
            return False


class Discount(Shop):
    discount_products =[]
    def __init__(self, discount_products, name, s_type):
        super().__init__(name, s_type)
        self.discount_products.append(discount_products)

    @classmethod
    def get_discount_products(cls):
        return cls.discount_products