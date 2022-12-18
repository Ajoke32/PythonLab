from classes import kms as k,plot as p
import csv
import re

class KmrWork(k.KmrCsv,k.Statistic,p.Plots):
    __kmrs={1:"./marks1.csv",2:"./marks.csv"}
    cat="kmr_results"
    def __init__(self, ref, num):
        super().__init__(ref,num)

    @classmethod
    def compare_csv(cls):
        compare_info={}
        compare_results=[]
        tuple_dict=("av_t","av_m")
        for x,y in cls.__kmrs.items():
            with open(y,"r") as f:
                result = csv.reader(f)
                avg_time=0
                avg_mark=0
                count=0
                for i in result:
                    res = re.findall("(\d+)", i[3])
                    to_min = float(res[0]) + float(res[1]) / 60
                    avg_time+=to_min
                    avg_mark+=float(i[4].replace(",","."))
                    count+=1
                compare_info[F"av_t{x}"]=round(avg_time/count,2)
                compare_info[F"av_m{x}"]=round(avg_mark/count,2)
        print(compare_info)

        compare_results.append("kmr count:2\n")
        for i in range(0,len(tuple_dict)):
            if compare_info[F"{tuple_dict[i]}{i+1}"]>compare_info[F"{tuple_dict[i]}{i+1}"]:
                compare_results.append(F"KMR 2 {tuple_dict[i]}({compare_info['av_t1']})>KMR 1 {tuple_dict[i]}({compare_info['av_t2']})\n")
            else:
                compare_results.append(F"KMR 2 {tuple_dict[i]}({compare_info['av_t1']})<KMR 1 {tuple_dict[i]}({compare_info['av_t2']})\n")
                
        with open("./kmr_results/compare_res.txt","w") as f:
            f.write("".join(compare_results))

    @classmethod
    def compare_avg_plots(cls,kmr1,kmr2):
        cls.avg_plot(kmr1)
        cls.avg_plot(kmr2)



