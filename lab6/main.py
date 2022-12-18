import os.path
import datetime
import time
import csv
import re

def validate_str(nums):
    for x in nums.split(): #
        if x.startswith('-') and x[1:].isdigit():
            continue
        elif not x.isdigit():
            print("Input correct numbers")
            return False
    return True

def make_list():
    nums = input("Enter int list(use space for two-digit or negative digit and ect. number):")
    if not validate_str(nums):
        return 0

    if " " in nums:  # якщо в рядку є пробіли
        nums = [int(i) for i in nums.split()]  # функція спліт переводить рядок розбитий по пробілам в лист
    else:  # якщо пробілів немає
        nums = " ".join(nums).split()  # розбиваємо рядок по пробілам і конвертуємо в лист
    return nums

#task_1
def write_numbers():
    if not os.path.isdir("files"): #якшщо не існує директорії
        os.mkdir(r"files")  #створити її
    with open("files/numbers.txt", "w") as f:  #відкриття файлу для записування, якщо файлу немає, то він створиться
        for x in range(1, 11):   #цикл до 10
            f.write(F"{x}\n")    #запис числа з нового рядка
    return 0


def read_numbers_sum():
    num_sum=0
    if not os.path.isdir("files"):
        os.mkdir(r"files")           #те саме, що і в попередній функції
    with open("files/numbers.txt","r") as r:  #відкриття файлу для записування, якщо фалу немає, то він створиться 
        for i in r:    #зчитування данних з файлів   
            num_sum+=int(i)  #додавння елементу до суми
        with open("files/sum_numbers.txt","w") as l: #відкриття для файлу для записування
            l.write(F"{num_sum}")  #запис суми в файл 
    return 0

write_numbers()
read_numbers_sum()
#task_1

#task_2
def sort_num(numbers):
    if not os.path.isdir("files"): #якщо папки немає
        os.mkdir(r"files")   #створити її
    with open("files/num_info","w") as f:  #відкриття файлу для читання
        for x in numbers:  #цикл по листу
            if x%2==0:   #якщо парне
                f.write(F"{x} - odd\n") #записуємо в лист з поміткою парне
            else:
                f.write(F"{x} - even\n")  #інакше не парне

num = make_list()
if num:
    sort_num(num)
#task_2

#task_3
def learm_python():
    text=""
    dic=dict()
    with open("files/learning_python","r") as f: #відкриття фалу для читання
        for x in f: #цикл по записам в файлі
            text+=x #всі записи в змінну текст
    arr = text.split("\n") #запис в массив по сепаратору
    for x in arr:  #цикл по масиво
        dic[len(x)]=x #запис у словник виду: "довжина":"рядок"
    mass = sorted(dic.keys(),reverse=True)  #сортування ключів(довжин кожного рядка) словника
    for i in range(0,len(mass)):   #цикл по довжині відсортованого масива
        print(dic[mass[i]])   #в словнику є всі ключи, які попередньо відсотовані в масиві, виводимо їх в правильному порядку

    return 0

learm_python()
#task_3

#task_4
def replace_language():
    text=""
    dic = dict()
    count =0
    with open("files/learning_python","r") as f:  #відкриття файлу для читання
        for x in f: #цикл по файлу
            text+=x  #в змінну заначення

        arr = text.split("\n") #ділимо по ентерам
        print("Enter T(true) or F(false) against statment") #повідомлення як потрібно проходити опитування
        for x in arr: #цикл по масиву значення
            replaced = x.replace('Python','C#')  #заміна в рядку пайто на сі шарп
            res = input(F"{replaced}:")   #зчитування відповіді на питання
            if res =='T' or res=='t': #якшо там тру
                dic[replaced]='T'   #в словник це твердження з значенням тру
            elif res=="F" or res=="f":
                dic[replaced] = 'F'     #вже те саме, але занчення фолс
            else:
                print("Enter correcct date!") #якщо відповідь не коректна
                return 0    #завершаємо програму
        os.mkdir("files/statement") #якщо ні, створюємо папку з твердженнями в поточному каталозі
        w='w'  #змінна для визначення, яким методом потрібно відкрити файл
        for x,y in dic.items(): #цикл по ключам і значенням
            if y =='T': #якщо значення тру
                if count>0: #і файл для запису відриваємо вперше
                    w="a"  #то потрібно дописати в кінець
                with open("files/learning_python",F"{w}") as f: #відкриття файлу з правдивими значенням и
                    f.write(F"{x}\n")  #запис у файл
                count+=1 #лічильник, шо позначає, що у файл вже були записані значення
            if y=='F': #якщо фолс
                with open("files/statement/f_statment.txt", "a") as f: #вікриваємо пустий файл
                    f.write(F"{x}\n") #записуваємо туди фолс-твердження

replace_language()
#task_4

#task_5
def create_geust():
    name = input("Enter your name:") #зчитування імені
    hi = F"Hello,{name}" #запис фрази в змінну
    print(hi) #вивід в консоль
    with open("files/guest_book","a") as f: #відкриття файлу
        #запис в змінну часу коли був створенний файл у форматі рік-місяць-день години:хвилини:секунди
        creted = datetime.datetime.fromtimestamp(os.path.getctime('files/guest_book')).strftime('%Y-%m-%d %H:%M:%S')
        #запис у замінну поточного часу, який і є останнім часом зміни файлу
        date=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #запис у файл всього, що створено вище
        f.write(F"{hi}, added:{date}, file was create:{creted}, changed:{date}\n")



for i in range(0,2):
    create_geust()
#task_5

#task_6
def get_statistic(word):
    text=""
    with open("files/python_publication","r") as f: #відкриття фалу з публікацією
        for x in f: #цикл по тексту
            text+=x.lower()  #запис тексту в змінну
    #знову отримання часу створення фалу
    created = datetime.datetime.fromtimestamp(os.path.getctime('files/publication_info')).strftime('%Y-%m-%d %H:%M:%S')
    start = time.perf_counter() #початок відліку
    freque = text.count(word.lower()) #частота з якою зустрічається слово
    end = time.perf_counter()  #кінець відліку
    total_time = F"{end-start}" #розрахунок часу
    print(F"\nSearch result, symbol/word '{word}' frequence: {freque}, search time:{total_time}\n")#інформація про пошук і заміну
    with open("files/publication_info", "a") as f: #відкриття файлу для запису
        f.write(F"[\nSearch result, symbol/word '{word}' frequence: {freque}, search time:{total_time}\n"
                F"file was created:{created}\n,last changes:{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n]\n")
        #запис туди результатів

get_statistic("a")
#task_6



#task_7
def studen_stat():
    cheked=[]
    result=[]
    entites = []
    with open('files/marks.csv', 'rt') as f: #відкриття цвс файлу для читання
            csvread = csv.reader(f)  #функція для читання цвс формату
            marks = [row for row in csvread] #записування у масив прочитаних данних
            print(F"number of students:{len(marks)}") #кількість студнтів
            for x in marks: #цикл по масиву з записами
                reg = re.findall("\"((\d+),(\d+))\"", "".join(x)) #заміна "3,23" на "3.23"
                res = "".join(x) #переформатування в стрінг
                for i in reg:  #по результатам регулярного виразу
                    if i[0] in cheked: #якщо оцінка уже є в масиві
                        continue   #перехід до наступної ітерації
                    res = res.replace(F"{i[0]}",F"{i[1]}.{i[2]}") #заміна всіх значень поточної цифри в потрібний формат
                    cheked.append(i[0])   #додавання в масив уже перевірених цифр
                cheked=[]  #для наступної ітерації
                result.append(res) # в результат записуємо знаячення в потрібному форматі
    sums = 0 #сума
    for x in result: #цикл по результатам
        entites.append("".join(x).split(",")) #запис в масив по сепаратору ",", щоб можна було працювати з даними
        sums = 0 #онулення
        for i in entites: #по масиву даних
            sums += float(i[4].replace("\"", "")) #щоб порахувати сумму видалення " та додавння до суми всіх балів

    print(F"student mark:{sums}") #інформація про суму всіх балів
    time_reg = re.findall("(\d+)", entites[0][3]) #пошук чисел в 1 рядку і 4 колонці(час)
    bal = re.findall("(\d+.\d+)", entites[0][4])  #пошук в 1 рядку і 5 колонці(бали)
    finish_time = round(float(time_reg[1]) / 60 + float(time_reg[0]), 2) #час коли студент завершив тест в хвилинах
    sec_min = float(time_reg[1]) / 60 #переведення секунд в хвилини

    print("student 1:")  #статистка для першого студента
    for i in range(1,int(time_reg[0])+1): #цикл по часу, на протязі якого студент ще писал тест
        #за час і, середній бал студента
        print(F"{round(i+sec_min,2)} min avarage {round((i+sec_min)*float(bal[0])/finish_time,2)}")
    correct = 0  #лічильник для коректних відповідей
    incorrect = 0 #і для не коректних
    question = 1 #номер питання
    for x in range(5, 25): #з 5 колонки по 25(цикл по всім балам)
        for i in entites: #цикл по масиву данних
            if float(i[x].replace("\"", "")) != 0: #якщо не нуль, значить на питання відповідь рівна
                correct += 1 #збільшення кількості правильних відповідей
            else:
                incorrect += 1 #збільшення кількості неправильних
        with open("files/question_statistic","a") as f: #відкриття файлу для запису
                #запис у файл статистики і-того питання
                f.write(F"question {question}: {round(correct * 100 / 170, 2)}%(correct)/{round(incorrect * 100 / 170, 2)}%(incorrect)\n")
        correct = 0
        incorrect = 0  #онулення для наступного питання
        question += 1  #інкремент питання

    time_marks =dict()
    extendet_time_info =dict()
    s=1
    for x in entites: #по массиву даних
        time_reg = re.findall("(\d+)", x[3]) #в 3 колонці шукається час
        bal = re.findall("(\d+.\d+)", x[4])  #в 4 оцінка
        finish_time = round(float(time_reg[1]) / 60 + float(time_reg[0]), 2) #час у минутах
        koef = float(bal[0])/finish_time #оцінка на час
        time_marks[F"student {s}"]=F"{round(koef,2)}"  #запис у словник студента і його коефіцієнту
        #щоб в подальшому легче було записати у файл все що потрібно
        extendet_time_info[F"student {s}"]=F"mark({bal[0]}),time({finish_time}m),koef({round(koef,2)})"
        s+=1 #інкремент студента(звучить страшно)

    arr = list(time_marks.values()) #запис в масив тільки коефіцієнтів студентів
    k=[]
    for x in range(0,5): #цикл з 0 по 5 для знаходження тих самих 5 студентів
        a = max(arr) #в масив найбільший коєфіцієт
        k.append(list(filter(lambda x:time_marks[x]==a,time_marks))) #пошук студента и запис в топ
        arr.remove(a) #видалення цього студента з масиву, щоб знайти залишившихся

    for i in k: #по масиву с топ-листом студента
        with open("files/question_statistic","a") as f: #відкриття файлу для запису
            f.write(F"{''.join(i)}:{extendet_time_info[''.join(i)]}\n") #запис туди інформації про студентів


studen_stat()

#task_7







