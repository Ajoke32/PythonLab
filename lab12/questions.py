import datetime
import random

class Questions:
    results=0
    __current=str
    __date=None
    def __init__(self, questioExam):
        self.__questions=questioExam.copy()
        self.__start_date=datetime

    @property
    def start_date(self):
        return self.__start_date

    @start_date.setter
    def start_date(self,date:datetime.datetime):
        self.__start_date=date

    def make_question(self):
        if not self.__questions:
            return False

        ques = random.choice(list(self.__questions.keys()))
        ques_str=F"{ques}:\n"
        self.__current=ques
        for x in self.__questions[ques]:
            ques_str+= F"{''.join(list(x.keys()))}\n"

        return ques_str


    def chek_result(self,answer):
        if not self.__questions:
            return False

        if answer in ['A', 'B', 'C', 'D']:
            for x in self.__questions[self.__current]:
                if ''.join(list(x.keys())).startswith(answer):
                    if list(x.values())[0]:
                        self.results = self.results + 1
                        self.__questions.pop(self.__current)
                        return True
                    else:
                        self.__questions.pop(self.__current)
                        return False
        else:
            self.__questions.pop(self.__current)
            return False


    def get_result(self):
        return F"Your results:{self.results}/10"

    def fill_question(self,newQuestions):
        self.__questions=newQuestions.copy()
        self.results=0




questions={
        "Python is":[{'A Сompiled language':False},{'B Interpreted language':True},
                     {'C Both of the statements are correct':False}, {'D Translated language':False}],

        "What is the difference between list and tuples in Python?":[{'A List can be edited but tupple no':False},
                                                                         {'B Tupple can be edited but list no':False},
                                                                     {'C Tuples are faster than list an 1st statement':True},
                                                                     {'D List are faster than tupple and 2nd statement':False}],
        "Local variable":[{"A Can be seen throughout programm":True},
                          {"B Visible only in certain places":False},
                          {"C It is a python type":False},
                          {"D Pythond does not support this":False}]
}



"""
,
    "MRO is": [{"A basic python class": False},
               {"B It is the order in which a"
                "method is searched for in a classes hierarchy": True},
               {"C Queue by which the interpreter reads the code": True},
               {"D A module that can launch puthon programm in another PC": False}],
    "Foreach in python": [{"A Is a type of cycle": False},
                          {"B Method that split a list to string": False},
                          {"C Not exist in Python": True},
                          {"D Long form of for cycle": False}],
    "Python attribute, chose correct form": [{"A __private,protected,_public": False},
                                             {"B __public,_private,protected": False},
                                             {"C In python all attributs is public": False},
                                             {"D __private,public,_protected": True}],
    "Can i get a private attribute in Python": [{"A Yes": True}, {"B No": False},
                                                {"C Python not suppurted pivate attribute": False},
                                                {"D Yes,with python libraries": False}],

    "How i can get all numbers from 4 to 25": [{"A foreach(1,24):print(each)": False},
                                               {"B for i in range(4,25):print(i)": False},
                                               {"C for (let i=0;i<=25;i++):print(i)": False},
                                               {"D for i in range(4,26):print(i)": True}],

    "MRO order computed:": [{"A From right to left": True}, {"B From left to right": False},
                            {"C By class order in the program": False},
                            {"D By the amount of memory that occupies the class": False}],

    "Chose only Pythin labraries": [{"A unittest,pycharm,flask,enityframework": False},
                                    {"B flask,numPy,cisco,django": False},
                                    {"C numPy,aiogram,flask,pytest": True},
                                    {"D vuePy,pyplot,random,SciPy": False}]


"""
