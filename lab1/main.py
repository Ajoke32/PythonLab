import math as m
#підключення бібліотеки для матиматичних функцій

a = float(input("enter value:"))
b = int(input("enter value:"))
c = int(input("enter value:"))   # зчитування даних з клавіатури та створення змінних
d = float(input("enter value:"))
numbers = [a+b, d-c, a*c, a/d, m.pow(b, d), int(a/d), a % d]  # запис результату виконаних операцій у створений список
print("Result a+b:", a+b)
print("Result d-c:", d-c)
print("Result a*c:", a*c)
print("Result a/d:", a/d)
print("Result pow(b,d):", m.pow(b, d))
print("Integer result a/d:", int(a/d))   # приведення типу для цілочисельного ділення
print("Result  a%d:", a % d)
print("Number of elements:", len(numbers))  # визначення довжини списку

for i in numbers:
    if i%2==0 and i!=0:   # виведення на екран парних елементів списку
        print(i)

tmp = numbers[1]
numbers[1] = numbers[4]   # зміна елементів 2 та 5 місцями
numbers[4] = tmp
print(numbers)

name = input("enter name:")
# зчитування прізвища та імя

print(f"Лабораторну роботу виконав {name}.\nНа данній лабораторній роботі я ознайомився з деякими особливостями"
      f" синтаксису мови програмування Python,\nнавчився створювати список та додавати в нього нові елементи,\n"
      f"ознайомися з функціями введення/виведення, дізнався які оператори доступні в мові програмування Python"
      f" та як їх застосовувати\n")  #виведення в висновку
