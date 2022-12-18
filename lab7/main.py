import json
import person as p


#перевірки для файлів не робив, тому працює тільки якщо файл в потбірному стані
def modifier(filename):
    persons=[] #лист з об'єктів
    with open(filename,"r") as f: #вікриття фалу для читання
        data = json.load(f)  #запис у змінну даних
        users = data['users'] #отримання листа з об'єктів

    for x in users: #икл по масиву з обєктами
        person_ex=p.Person(x['name'],x['surname'],x['birthday']) #створення екзкмляра
        persons.append(person_ex) #додавання до листа обьєкта

    for x in range(0,len(persons)): #цикл для встановлення данних
        fullname = persons[x].get_fullname() #отримання імя та прізвища з і-того об'єкта
        age = persons[x].get_age()   #отриманя віку
        users[x]['nick']=persons[x].nickame #запис в і-тий обьекте нового поля нік
        users[x]['fullname']=fullname   #запис нового поля фулнейм
        users[x]['age']=age #запис ейдж
    data['users']=users #оновлення обьектів в початковому листі
    with open(filename,"w") as f: #відкриття файлу для запису
        json_obj = json.dumps(data,indent=2) #переведення в джейсон формат
        f.write(json_obj) #запис обєкта в файл

modifier("user.json")


