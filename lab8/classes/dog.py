class Dog:
    mammal="yes"
    nature="not set" #атрибути класу
    breed="not set"

    def __init__(self,name, age): #ініціалізація атрибутів
        self.name=name
        self.age=age

    def get_info(self):
        return F"Name: {self.name} Age: {self.age}" #отримання інформації про собаку

    @staticmethod
    def voice():
        return "Gaf" #собака подає голос

    def make_somersault(self):
        if self.age>10:  #якщо собаці більше ніж 10 років
            return "your dog broke his leg" #вона робить сальто та ламає ногу

    @staticmethod
    def move():
        return "i'm going" #собака рухається

class BelgainSheepDog(Dog): #бельгійська собака
    nature = "kind" #характер
    breed = "Belgain Sheep" #порода

    def breathe_fire(self):
        if self.age<4: #якщо років менше ніж 4
            return F"I still can't do it" #собака не може дихати вогнем
        else: #інашке
            return "Arrr" #може

class AmericanBuldog(Dog):
    nature = "angry" #все те саме, але інші значення
    breed = "American Buldog"
    def hunt(self): #методо полювати
        return F"i'm {self.nature} hunter"
