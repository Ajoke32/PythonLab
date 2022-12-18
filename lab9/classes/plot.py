import os
import numpy as np
import matplotlib.pyplot as plt


class Plots:
    __cat_ref=""
    @classmethod
    def set_cat(cls,name):
        os.mkdir(F"./{name}")
        cls.__cat_ref=F"./{name}"

    @classmethod
    def avg_plot(cls,makrs_pesent):
        data = dict()
        l=1
        for x in range(0,len(makrs_pesent)):
            data[F"q{x+1}"]=makrs_pesent[x]
        questions=list(data.keys())
        qus_result=list(data.values())
        if os.path.isfile(F"./question_stat/question_stat{l}.png"):
           l+=1
        cls._make_bar(questions,qus_result,"questions","persents","questions result",F"question_stat{l}")

    @classmethod
    def marks_plot(cls,student_marks):
        marks=student_marks.keys()
        students_count=student_marks.values()

        cls._make_bar(marks,students_count,"makrs","students count","marks statistics","marks_statistics","green")


    @classmethod
    def _make_bar(cls,xdate,ydate,xlabel,ylabel,title,graphname,color="orange"):
        figure = plt.figure(figsize=(15, 5))
        plt.bar(xdate, ydate, color=color)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        figure.savefig(F"{cls.__cat_ref}/{graphname}.png")

    @classmethod
    def best_marks_plot(cls,best_marks):
        data= {}
        for x in best_marks:
            stat = x.split(",")
            data[stat[0][0:5]]=stat[2]
            print(stat[2])
        cls._make_bar(data.keys(),np.arange(0.29,0.30,),"student id","makrs","best_5 ","best 5 statistic","blue")

