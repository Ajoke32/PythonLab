class Car:
   def __init__(self, mark, model, year): #ініалізяція
       self.mark=mark
       self.model=model #присвоєння атрибутам значень
       self.year=year
       self.speed=0

   def accelerate(self):
        self.speed+=5 #додавання до швидкості

   def brake(self):
       self.speed-=5 #віднімання до швидкості

   def get_speed(self):
        return self.speed #поточна швидкість
