import math


# taks1
def get_interval_number(a, b, c):
    arr = [a, b, c]  # запис даних в лист
    return list(filter(lambda x: x >= 1 and x <= 3, arr))  # фільтрація масиву для заданого діапазону

print(get_interval_number(4, 2, 3))  # результат виконання функції


# task1

# taks2
def check_year(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0): #перевірка на високосний рік та повернення 366
        return 366
    else:
        return 365  #якщо рік не вискосний повертаемо 355


print(check_year(2022))


# task2

# taks3
def get_discount(suma):
    if 500 < suma < 1000: #якщо сума в діапазоні від 500 до 1000
        suma = suma - (suma * 3 / 100) #рахуемо знижку 3 відсотка
        print(f"Discount 3%! Your final sum: {suma}")
    elif suma > 1000: #якщо сума більше 1000
        suma = suma - (suma * 5 / 100)   # рахуємо знижку 5 відсотків
        print(f"Discount 5%! Your final sum: {suma}")


get_discount(1001)


# task3

# taks4
def calculate_min_cos(a, b, c, d):
    arr = [a, b, c, d] # заносимо дані в лист
    return math.cos(min(arr)) # за допомогою функції мін шукаємо мінімальний елемент та рахуемо його косинус


print(calculate_min_cos(12, 4, 8, 5))


# task4#
# taks5
def get_max_sin(a, b, c):
    arr = [a, b, c] # заносимо дані в лист
    return math.sin(max(arr)) # за допомогою функції мах шукаємо максимальний елемент та рахуемо його сінус


print(get_max_sin(4, 12, 3))


# task5

# taks6

def calculate_s(height, sides):
    s = 1 / 2 * float(sides) * float(height) # рахуємо площу
    if s % 2 == 0: # якщо площа ділиться на 2, повертаємо результат
        return s / 2
    else:
        return "I can't divide this" #інакше виводимо повідомлення, що я не можу ділити це


print(calculate_s(4, 2))


# task6

# task7
def get_year_name_by_number(number):
    # словник місяців
    month = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
             9: "September", 10: "October", 11: "November", 12: "December"}
    if not number in month: # якщо в словнику немає такого ключа, пишемо, зо місяця нема
        return "month not exist"

    return F"You month is {month[int(number)]}"


# task7
print(get_year_name_by_number(10))


# task8
def get_positive_number(a, b, c):
    arr = [a, b, c] # заносимо дані в масив
    return len(list(filter(lambda x: x > 0, arr))) #фільтрація масиву якщо елемет більше 0,тобто додатній
    # поветаємо довжину, тому що в списку залишаться тільки ті елементи які прошли умову


print(get_positive_number(2, -10, 4))


# task8

# task9
def get_sum_integer(a, b):
    sum = 0
    if b < a: # якшо б менше, повертаємо помилку
        return "invalid value b"
    for i in range(a, b + 1): #якщо все ок, проходимо по елементам від а до б
        print(i)
        sum += i # послідовно додаємо

    return sum


print(get_sum_integer(3, 10))


# task9


# task10
def get_quadrat_integer(a, b):
    sum = 0
    if b < a:
        return "invalid value b"   #теж саме, що в 9 завданні,тільки в суму записуємо квадрат чисел
    for i in range(a, b + 1):
        sum += math.pow(i, 2)

    return sum


print(get_quadrat_integer(1, 3))


# task10#


# task11
def get_average():
    sum = 0
    a = input("Enter a:") #зчитуємо а
    for i in range(int(a), 201): # від а до 200
        print(i)
        sum += int(a)  # сума числе

    return F"result:{sum / 200}" #середнє занчення


print(get_average())


# task11

# task12
def get_sum_for_range(a, b):
    sum = 0
    if b < a:
        return "invalid value b"
    while a <= b: # поки а більше рівне б
        sum += a # сумуємо елементи
        a += 1   # інкрементумо лічильник
    return sum


print(get_sum_for_range(2, 5))


# task12


# task13
def get_quadratic(a):
    sum = 0
    if (a < 0 or a > 50):
        return "error invalid value a" # якщо а не впадає в діапазон повертаємо помилку
    for i in range(a, 51): # якщо все ок
        print(i)
        sum += math.pow(i, 2) # рахуємо суму квадратів
    return sum


c = int(input("Enter value:"))
print(get_quadratic(c))


# task13


# task14
def get_min_number_k(n):
    i = 0
    if n < 1:
        return "error invalid value" #перевірка що Н більше 1

    while math.pow(5, i) <= n: # поки 5 в K менше Н інкрементуємо і
        i += 1

    return i


print(get_min_number_k(12))


# task14


# task15
def get_number_for_n(n):
    l = 1
    sum = 0
    for i in iter(int, 1): #нескільнченний цикл
        sum +=l #сума послідовності
        l += 2 #інкрементація змінної л на 2
        if sum > n: # якщо сума більше н, виходимо с цикла
            break
    return sum #повертаємо суму


print(get_number_for_n(1))


# task15

# task16
def get_number_while_n(n):
    i = 1
    sum = 0
    while n >= sum: #поки н більше рівне сумі
        sum += i
        if (i == 1):  # для 1 операції інкрементуємо і на 4
            i += 4
        i += 2  # для всіх інших на 2


    return sum # повертаємо суму


print(get_number_while_n(12))
# task16
