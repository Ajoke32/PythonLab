
class ExceptionEx(ValueError): #класс наслідуваний від ValueError

    def __init__(self, message="name lenght less than 10"): #ініціалізація
        self.__message=message
        super().__init__(self.__message) #передча в базовий класс повідомлення про помилку



