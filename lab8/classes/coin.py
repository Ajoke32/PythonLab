import random


class Coin:

    def __init__(self,side): #ініціалізація
        if side == 'heads' or side == 'tails': #якщо сторона введена корректно
            self.__sideup=side #присвоюємо атрибуту сторону
        else:
            self.__sideup = "Side not exist!" #якщо ні, присвоэння атрибуту значення про неыснування сторони
            print("Side not exist!")  #повідомлення, що сторони не існує

    def toos(self):
        if self.__sideup!='Side not exist!': #якщо монета ініціалізована правильно
            x = random.randrange(1,213124) #вибираємо рандомне числе
            if x%2==0: #якщо воно ділиться на 2
                print("reshka") #решка
            else:
                print("orel") #інашке орел

