class RomanToIneger:
    __roman_map={ #словник з шифруванням римських чисел
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }

    def __init__(self, text): #ініціалізація
        self.text=text

    def to_int(self): #метод для переводу
        number = 0
        i=0
        while i<len(self.text): #цикл по тексту
            if i + 1 < len(self.text): #якщо і це не останній символ
                #якщо наступне число більше за попереднє
                if self.__roman_map[self.text[i]] < self.__roman_map[self.text[i + 1]]:
                    #до числа потрібно додати різницю наступного числа від поточного
                    number += self.__roman_map[self.text[i + 1]]-self.__roman_map[self.text[i]]
                    i+=2 #оскільки ми прошли 2 числа, потрбіно перепригнути через 1
                else: #інакше
                    number += self.__roman_map[self.text[i]] #просто додаємо поточне значення числа
                    i+=1
            else: #якщо це останнє значення
                number += self.__roman_map[self.text[i]] #просто додаємо
                i+=1
        i+=1
        return number #поветаємо результат

class IntToRoman:
    num = [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000] #инт числа
    sym = ["I", "IV", "V", "IX", "X", "XL",
           "L", "XC", "C", "CD", "D", "CM", "M"] #римські числа

    def __init__(self, number): #ініціалізація
        self.number=number

    def printRoman(self):
        i = 12  #проходимось по спискам з кінця
        while self.number: # поки число не 0(в данному випадку)
            div = self.number // self.num[i] #цілочисельно ділимо число на і-те число зі списка чисел
            self.number %= self.num[i] #процент ділення вхідного числа на і-те число, записуємо у поточне число
            while div: #якщо цілочисельне ділленя не 0, значить число можна розбити та вивести римське представлння
                print(self.sym[i], end="") #вивід цього числа в римському представленні
                div -= 1 #для наступних перевірок
            i -= 1

