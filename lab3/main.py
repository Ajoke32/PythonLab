import sys as s

def make_str(text, to_lower=bool(1)): # функуція для очистки лишніх символів із рядка
    if(to_lower==bool(1)): # якщо для завдання не потрібні великі літери
        a = text.lower()  # весь текст в до нижнього регістру
    else:
        a = text  #інакше залишаємо текст без змін
    i = 0 # лічильник
    while i < len(text): #поки і менше довжини рядка
        if not text[i].isalpha(): # якщо символ не є числом
            a = a.replace(text[i], " ") #замінюємо його на пробіл

        i += 1 # інкрементація лічильника

    return " ".join(a.split()) #перетворення рядка до листа, щоб позбудтися лишніх пробілів та перетворення обратно в рядок
    #, що розбитий без лишніх пробілів

def check_str(text): # перевірка на корректність даних
    if not isinstance(text, str): #якщо ти даних не стрінг
        print("Value must be of type str") # помилка
        s.exit() # дострокове завершення програми


#task1
def get_count_contain_value(text):
    check_str(text)
    text = make_str(text)   #перевірка та перетворення вхідних даних
    symbol = input("Enter value:") #зчитування символа для сортування
    return len(list(filter(lambda x:x.startswith(symbol.lower()) and len(x)>2, text.split(" "))))
    # повернення довжини листа слів які прошли фільтрацію
print(get_count_contain_value("This text contain word that stratwith t"))
#task1

#task2 and 4
def replace_values(text, value, replace_value, get_count_symbol=bool(0)): # функція для заміни символа
    check_str(text) # перевіка
    if get_count_symbol == bool(1): #якщо потрібно рахувати кількість символів в рядку
        return F"Result:{text.replace(value, replace_value)}\nNumber of changes:{text.count(value)}\n" \
               F"Symbols count:{len(text.replace(' ', ''))}"
    else: #якщо не потрібно
        return F"Result:{text.replace(value, replace_value)}\nNumber of replaced values:{text.count(value)}"
#task2 and 4

#task2
print(replace_values("She said:la-la-la, definition:this func....", ':', '%')) #без підрахунку символів
#task2
#task3 and 6
def delete_value(text, value):
    check_str(text)
    return F"Result:{text.replace(value, '')}\nNumber of deleted values:{text.count(value)}" #заміна значень та кількості замін
#task3 and 6

#task3
delete_value(".text write this.another things. tin.ten.", '.')
#task3

#task4
print(replace_values("apple no watch master", 'a', 'o', get_count_symbol=bool(1)))#заміна з підрахунком символів
#task4

#task5
def to_lower(text):
    check_str(text)
    return text.lower() #повенення рядка в нижньому регістрі

print(to_lower("Asdvdf dsadFdsda EqEWERsd fsd"))
#task5

#task6
print(delete_value("how old are you?", 'o')) #видалення із тексту символа
#task6

#task7
def replace_p(text):
    check_str(text)
    text = make_str(text)  # перевірка та очистка рядка
    a = "".join(list(text)[0:int(len(text)/2)+1]) #запис у змінну а першу половину рядка n/2
    text = text.replace(a, a.replace('п', '*')) # заміна першої частини у тексту, змінною а, де замінені всі п
    return text #поверенення результату

print(replace_p("практикуємо практику нпa практиці без практики"))
#task7

#task8
def get_count_word(text,word):
    check_str(text)
    return text.count(word) #повернення кількості заданих слів/символів

print(get_count_word("на в у б на (на) ыбс наы (((на.......", "на"))
#task8

#task9
def make_title(text):
    check_str(text)
    return text.title() # функція title переводить всі перші сиволи рядка у верхній регістр

print(make_title("make this string to title"))
#task9

#task10
def get_sort_word(text, start, end):
    check_str(text)
    text = make_str(text)
    return list(filter(lambda x:x.startswith(start) or x.endswith(end), text.split(" ")))
    #фільтрація списку за умовою що слово починається з символа start, або закінчується символом end
print(get_sort_word("English wish pot google docs dack","d","h"))
#task10


#task11
def get_voice_symbol(text):
    i=0
    text = make_str(text)
    voice = "aeiouy" # рядок голосних літер англ алфаіту
    for x in text: # пробігаємося по заданому рядку
        if voice.count(x)>0: #якщо буква присутня в рядку голосних букв
            i+=1 # інтрементація кількості голос. букв

    return i

print(get_voice_symbol("test text to find or sort"))
#task11

#task12

def get_not_voice_symbol(text):
    i=0
    text = make_str(text)
    not_voice = "bcdfghjklmnpqrstvwxz" #теж саме, тільки рядок з приголосними
    for x in text:
        if not_voice.count(x)>0:
            i+=1

    return i

print(get_not_voice_symbol("test text to find or sort"))
#task12

#task13
def get_name_upper(text):
    text = make_str(text, bool(0))
    print(text)
    return list(filter(lambda x:x.istitle(), text.split(" ")))
    # функція istitle перевіряє чи перша літера слова у верхньому регістрі
print(get_name_upper("I visted this countries 3 times: ((Italy((, Spain, Swizerland"))
#task13
