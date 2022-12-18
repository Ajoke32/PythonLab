import csv
import re

class KmrCsv:

    def __init__(self,ref="./marks.csv",num=2):
        self.num=num
        self.ref=ref

    def set_ref(self,ref):
        self.ref=ref


    def get_ref(self):
        return self.ref

    def set_kmr_num(self,num):
        self.num=num

    def get_kms_info(self):
        count=0
        with open(self.ref) as f:
            read = csv.reader(f)
            for x in read:
                count+=1

        return F"KMR number {self.num}, student count:{count}"



    def get_kmr(self):
        makrs_res=[]
        with open(self.ref) as f:
            result = csv.reader(f)
            for x in result:
                makrs_res.append(x)

        return makrs_res


class Statistic:

    def __init__(self,kmr):
        self.kmr=kmr

    def avg_stat(self):
        correct=0
        stat=[]
        marks = self.kmr.get_kmr()
        for i in range(5,25):
            for x in marks:
                if x[i]!="0,00" and re.search("(\d,\d+)",x[i]):
                    correct+=1
            stat.append(round(correct*100/112,2))
            correct=0
        return tuple(stat)

    def marks_stat(self):
        marks=self.kmr.get_kmr()
        marks_dict=dict()
        for x in marks:
            if x[4] in marks_dict:
                marks_dict[x[4]]+=1
            else:
                marks_dict[x[4]]=1
        return marks_dict

    def marks_per_time(self):
        marks=self.kmr.get_kmr()
        time_dict = dict()
        for x in marks:
            res = re.findall("(\d+)",x[3])
            to_min =float(res[0])+float(res[1])/60
            time_dict[x[0]]=round((1*float(x[4].replace(",",".")))/float(to_min),2)
        return time_dict

    def best_marks_per_time(self,bottom,top):
        marks=self.kmr.get_kmr()
        per_time=self.marks_per_time()
        marks_for_range=dict()
        top_five=[]

        for x in marks:
            mark = float(x[4].replace(",","."))
            if top >= mark >= bottom:
                marks_for_range[F"{x[0]},{mark}"]=per_time[x[0]]

        marks_values = list(marks_for_range.values())
        marks_keys=list(marks_for_range.keys())
        for x in range(0,5):
            max_res=min(marks_values)
            position=marks_values.index(max_res)
            top_five.append(F"{marks_keys[position]},{max_res}")
            marks_values.remove(max_res)
        return tuple(top_five)
