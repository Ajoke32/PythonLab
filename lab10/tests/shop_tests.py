from online_shop import shop

example=shop.Shop('Gucci','Clothes')
discount=shop.Discount(['cocktail','fish'],example.shop_name,example.store_type)
def test_shop_description():
    assert example.describe_shop()=='Gucci Clothes'

def test_unit_setting():
    assert example.set_number_of_units(-1)=="invalid value!"
    assert example.set_number_of_units(1)=="units was be added!"

def test_increment_units():
    assert example.increment_number_of_units(-1)==False
    assert example.increment_number_of_units(0)==False
    assert example.increment_number_of_units(1)==True

def test_disply_dicsount():
    assert discount.get_discount_products()==['cocktail','fish']