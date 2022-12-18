import datetime as d
import re


class Person: #оголошення класу

    def __init__(self,name,second_name,birthday,nick="not set"): #функція для ініціалізації атрибутів
        self.birth_date = self.__check_date(birthday)
        self.first_name = name,
        self.surname = second_name,      #атрибути
        self.nickame=nick

    @staticmethod
    def __check_date(date):  #статичний приватний метод для валідації дати
         res = re.findall("(\d{4})-(\d{2})-(\d{2})",date) #пошук дати за форматом р-м-д
         if res: #якщо дата валідна
             try:
                 return d.date(int(res[0][0]), int(res[0][1]), int(res[0][2])) #спроба її створити та повернути
             except ValueError:
                 return "not set" #якщо в даті що не так з днем/роком/місяцем то в атрибут встановиться це повідомлення
         else:
             return "not set" #якщо формат не вірний теж саме що і зверху

    def get_fullname(self): #просто метод, який повертає імя та прізвище
        return F"{''.join(self.first_name)} {''.join(self.surname)}"

    def get_age(self): #метод, що повертає вік
        if isinstance(self.birth_date,d.date):
            diff = d.date.today()-self.birth_date #різниця між сьогоднішньою датою і дн
            return F"{round(diff.days/365)}" #рорзахунок різниці в роках
        else:
            return "You have a problem with your date input!" #якщо дата була введене не корректно



