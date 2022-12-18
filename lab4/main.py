import math

import numpy
import random


def validate_str(num):
    for x in num.split(): #
        if x.startswith('-') and x[1:].isdigit():
            continue
        elif not x.isdigit():
            print("Input correct numbers")
            return False
    return True

def make_list():
    num = input("Enter int list(use space for two-digit or negative digit and ect. number):")
    if not validate_str(num):
        return 0

    if " " in num:  # якщо в рядку є пробіли
        num = [int(i) for i in num.split()]  # функція спліт переводить рядок розбитий по пробілам в лист
    else:  # якщо пробілів немає
        num = " ".join(num).split()  # розбиваємо рядок по пробілам і конвертуємо в лист
    return num


def list_reverse(list_t):
    list_t = [int(i) for i in list_t]  #преведення елементів до інта, щоби порахувати максимальний елемент
    list_t.reverse()  #функція для переписання елементів у зворотньому порядку
    return F"Reversed list:{list(list_t)}\nmax element:{max(list_t)}"

numbers = make_list()
if numbers!=0:
    print(list_reverse(numbers))
#task_1



def rewriter(numbers):
    print(F"Initial list:{numbers}\nList with positive digit:{list(filter(lambda x:x>0,numbers))}"
          F"\nList with negative digit:{list(filter(lambda x:x<0,numbers))}")
    # просто за допомогою фільтра сортуємо за відповідною умовою листи
numbers = make_list()
if numbers!=0:
    rewriter(numbers)
#task_2

def odds_list_sum(numbers):
    summa = 0
    for i in range(0,len(numbers)+1):  # пробігаємось по листу
        if i%2!=0:  #якщо індекс не парний 
            summa+=numbers[i]  #сумумо елементи
    return summa

print(odds_list_sum(random.sample(range(1,25),20)))
#task_3


def sort_list(numbers):

    max_elem = max(numbers) # за допомогою функції мах знаходимо мах елемент листа
    sorted_list = list(filter(lambda x:x%2!=0,numbers)) # сортуемо лист по непарних елементах
    sorted_list.sort(reverse=True) #сотуемо за спаданням
    if len(sorted_list)<0:  #якщо массив порожній
        print("Absend odd element in list") #відповіднке повідомлення

    return F"Initial list:{numbers}\nMax element:{max_elem},index:{numbers.index(max_elem)}\nOdds element list:{sorted_list}"

print(sort_list(random.sample(range(-100,100),30)))
#task_4

def pairs_list(numbers):
    print(numbers)
    for x in range(0,len(numbers)+1):  #цикл для проходу по даному листу
        txt =""  #змінна для запису пар
        if x+1<len(numbers):  #в останнього числа ніколи не буде наступного елемету, в листі також, щоб уникнути помилки
            if numbers[x]<0 and numbers[x+1]<0:  #якщо поточна цифра відємна і наступна також
                current_num = numbers[x]  # поточний елемент
                txt+=F"{current_num} have pairs:{current_num}/{numbers[x+1]}" #записуємо що в поточного елемента є пара
                if x!=0: #якшо це не перша ітерація
                    if numbers[x-1]<0: #дивимось чи в поточний елемент утворює пару з попереднім
                        txt+=F" and {current_num}/{numbers[x-1]}" #якщо так записуємо у список його пар
                print(F"{txt}") #результат
        txt ="" #для подальшого запису

pairs_list(random.sample(range(-100,100),30))
#task_5

def max_elem_comp(numbers):
    max_el = max(numbers)  #знаходження макс елементу
    qua = list(filter(lambda x:x!=max_el,numbers)) #всі елементи що менші макс
    return F"Max:{max_el}\nListQ:{list(map(lambda x:x**2,qua))}"  #квадрати всіх менших чисел

print(max_elem_comp([5,12,32,4,9,25,14,35,8,23]))

def min_elem(numbers):
    module = list(map(lambda x:math.fabs(x),numbers)) #модуль всіх чисел
    module.sort() #сортування
    return F"Min:{min(module)}\nSort list:{module}"
    
a = []
for i in numpy.linspace(-100, 100, num=30, endpoint=False): #цикл для заповнення масиву числами
   a.append(round(i,2))

print(min_elem(a))
#task_7


def make_multiply_lists(numbers):

    a =[]
    dic = dict()
    sum = 0
    for x in range(1,31):
        sum+=math.fabs(numbers[x-1])
        a.append(numbers[x-1])
        if x%3==0 and x!=0:
            dic[F"{round(sum)}"]=a
            a=[]
    keys = [int(i) for i in dic.keys()]
    keys.sort()
    for i in range(0,len(dic)):
        print(F"{dic[F'{keys[i]}']} sum={keys[i]}")


b=[]
for i in range(0,30):
   b.append(round(random.uniform(-100,100),2)) #цикл для заповнення масиву числами
make_multiply_lists(b)
#task_8

