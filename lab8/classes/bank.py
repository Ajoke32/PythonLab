class Bank:

    def __init__(self, balance):  #метод для ініціаліації рахунку
        self.__balance = balance  #присвоєння атрибуту значення

    def put(self, amount): #метод для поповнення рахунку
        if  amount>0: #якщо сума не відємна
            self.__balance+=amount #попвнюється баланс на цю суму
            return F"{amount} put in your account" #повідомлення про внесення коштів на рахунок
        else: #якщо число відємне
            return "Please, enter valid digit!" #повідомлення про помилку

    def withdraw(self, amount): #метод для зняття коштів
        if self.__balance>=amount: #якщо сума знантя більше або рівна балансу
            self.__balance-=amount #знімаються кошти
            return F"{amount} withdrawn from your account" #повідомлення про зняття коштів
        else:
            return "Not enought money in you bank account" #інакше повідомлення про те, що на балансі недостатнью коштів

    def get_balance(self): #отримання балансу
        return F"You balance: {self.__balance}" #кошти на рахунку
