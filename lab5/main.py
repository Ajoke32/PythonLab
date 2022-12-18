import math
import time
import random


def get_spa():
    arr = dict() #словник щоб записати 3 прямокутника
    for i in range(0, 3): #цикл для ініціалізації 3 прямокутників
        a = input("Enter 2 sides(use space):")  #зчитування 2 сторін
        if len(a.split()) < 2 or len(a.split()) > 2:  # якщо більше 2 або меньше
            return "Please,enter 2 int numbers with space!"   #повертається помилка
        arr[F"S rect {i + 1}"] = a.split()   #якщо все ок записуємо сторони прямокутника
    for i in range(0,len(arr)):  #цикл по прямокутниках
        tmp = arr[F"S rect {i+1}"]  #тимачачсова змінна для зручності
        s = float(tmp[0])*float(tmp[1])  #сторна * сторону
        arr[F"S rect {i + 1}"] = s    #в відповідний прямогутник результат площі
    return  arr   #поверенення словника з рішеннями

print(get_spa())
#task_1


def trigon_solver(**kwargs):
    dic = dict()  #словник щоб записати гіпотенузи
    i=1
    for a,b in kwargs.values():    #цикл по значенням
        c = math.sqrt(pow(a,2)+pow(b,2))  #формула для знаходжння гипотенузи
        dic[i]=c  #гіпотенуза 1 трикутника
        i+=1

    if dic[1]==dic[2]: #якщо рівні гіпотенузи
        return F"hypotenuse trigon1:{dic[1]}=hypotenuse trigon2:{dic[2]}"
    if dic[1]>dic[2]:  #якщо 1 більша2
        return F"hypotenuse trigon1:{dic[1]}>hypotenuse trigon2:{dic[2]}"
    else:  #якшо 2 більше 1
        return F"hypotenuse trigon1:{dic[1]}<hypotenuse trigon2:{dic[2]}"

print(trigon_solver(first=[4,4],second=[4,5]))
#task_2

def enter(x,y): #функція для розрахунку належности точки
    x1=0
    y1=0
    r2 = pow(x1 - 5, 2) + pow(y1 - 3, 2)  #формула з завдання з рандомними значеннями
    points = math.sqrt(pow(x, 2) + pow(y, 2))  #довжина відрізка від 0 до точки
    if points > r2: #якщо відрізок більше,то
        return F"point({x},{y}) not enter" #точка за межами
    else: #інакше
        return F"point({x},{y}) enter"  #входить в коло

def get_points_in_circle(**kwargs):
    for x,y in kwargs.values():  # цикл по значенням
        print(F"{enter(x,y)}")  #результати робботи функції вище

get_points_in_circle(p=[40,5],f=[10,10],l=[5,5])
#task_3

def rectange(x,y,z,t):
    c = math.sqrt(pow(x,2)+pow(y,2))  #гіпотенуза для Х У
    check = pow(x,2)+pow(y,2)-pow(c,2) # для коду нижче
    if check==0: # якщо сума квадратів катетів мінус гіпотенуза дорівнює нулю, значить трикутник прямокутний
        trigon_s1 = x*y/2  #розрахунок першої половини прямокутника(1 трикутника)
        p = (z+t+c)/2   #півпериметр
        trigon_s2 =math.sqrt(p*(p-z)*(p-t)*(p-c)) #по формулі Герона 2 половина прямокутника
        s = trigon_s1+trigon_s2 #додаємо площі трикутників і отримуємо площу прямокутника
        return s

    return "angle X and Y !=90" #якщо провірку не пройде, то кут між Х У не 90

print(rectange(6,5,10,8))
#task_4


def divides_num(n,args):
    arr=[]
    count =0
    for i in range (1,n+1): #цикл по заданому діапазону н
        for x in args:  #цикл по цифрам
            if i%x==0:   #якшо число з діапазону до н ділиться на задане числo
                count+=1  #збільшуємо лічильник
        if count==len(args): #якщо лічильник дорівнює довжині списка, значить число з діапазону ділиться на всі задані числа
            arr.append(i)   #записужмо це число
        count = 0  # для викорисння в наступному циклі
    if len(arr)>0: #якщо такі числа є в діпазоні
        return arr  #повертаємо результат
    else:  #якшо ні
        return "Number not found" #повертаємо, що таких цифр немає

numbers = input("Enter numbers(use space):")
numbers = list(map(lambda x:int(x),numbers.split()))
print(divides_num(100,numbers))
#task_5


def calc_time(func):  #дкоратор для обрахунку часу,що приймає функцію на вхід
    def wrapper(): # обгортка
        start = time.perf_counter()  #початок відліку
        func()  #виклик поданої функцію
        end = time.perf_counter() #кінець відліку
        print(F"time:{end-start}")  #розрахунок часу

    return wrapper()   #поверенення функції/рузлтату


@calc_time  #автоматичне застосування декоратора
def get_divedes_interval():
    n = int(input("enter n:"))
    m  = int(input("enter m:"))
    dic = dict()
    arr=[]
    count=0
    for i in range(n,m):  # цикл від н по м
        for x in range(1,i+1):  #цикл по числу, макс. число що можна поділити на задане число без остачі це і є саме число
            if i%x==0: #якщо ділиться
                count+=1 #кількість дільників збільшуться
        if count>0: #якщо дільники є
            dic[count]=i #в ключ записуємо кількість дільників, а в значення саме число
            count=0
    max_v = max(dic.keys()) #максимальне число із кількості дільників
    return F"Number {dic[max_v]} have max div {max_v}"
#task_6

def get_simple_num(n):
    count =0
    arr=[]
    for x in range(1,n+1):
        for i in range(1,x+1): #все як і в попередньому завданні
            if x%i==0:
                count+=1
        if count==2: #просте число це число що ділиться на себе і на 1. значить в попреденьому циклі повинно поділитися рівно 2 рази
            arr.append(x)
        count =0
    a = int(input("Chose print mode 1.List 2.Strings 3.Count of simple numbers:"))
    if a==1:
        print(list(arr))
        return list(arr) #вивід листом
    if a==2:
        k = ""
        for i in range(0,len(arr)):
            k+=F"{str(arr[i])} "  #порядково, в кожному рядку по 5
            if i%5==0:  #в кожному рядку по 5
              print(k)
              k=""
    if a==3:
        print(len(arr))
        return len(arr)  #кількість таких чисел в діапазоні


get_simple_num(200)
#task_7

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




@calc_time
def generate_lists():
    init_list = make_list()  #початковий спосок
    max_v = max(init_list) #макс
    min_v = min(init_list) #мін
    new_list = make_list() #список що водиться другий раз
    check = list(filter(lambda x:x>=max_v or x<=min_v,new_list)) #перевірка чи там немає чисел більше макс і меньше мін
    if len(check)>0: #перевірка чи там немає чисел більше макс і меньше мін
        return "number in sequence must be max>number<min" #якщо є такі цифри помика
    bottom = min(new_list) #bottom
    upper = min(new_list) #upper
    final_list = random.sample(range(min_v+bottom,max_v-upper),15) #15 радндомних числе із діапазонів
    return 0
#task_8
#1 12 67 35 8 9    10 17 62 13 4




