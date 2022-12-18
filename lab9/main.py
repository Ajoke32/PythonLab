import os
from classes import plot as p
from classes import alphabet as ap
from classes import human as h
from classes import apple as a
from classes import kms as k
from classes import kmrwork as w

eng = ap.EngAlphabet("example","en","abcdefghijklmnopqrstuvwxyz")

print(eng.print_alphabet())
print(eng.letters_num())
print(eng.is_en_lang("J"))
print(eng.is_ua_lang("Щ"))
print(eng.example())


print(h.Human.default_info())
human = h.Human("Alex",20,30000,h.House(200,650000))
print(human.info())
small = h.SmallHouse(40000)
print(human.buy_house(small,12))
human.earn_money(770000)
print(human.buy_house(small,12))
print(human.info())



apple1=a.Apple(0)
apple2=a.Apple(1)
apple3=a.Apple(3)
apple4=a.Apple(4)
apple5=a.Apple(5)

tree = a.AppleTree(5)
gardener = a.Gardener("Mike",tree)
gardener.apple_base()
gardener.work()
gardener.harvest()
gardener.work()
gardener.work()
gardener.work()
gardener.harvest()




kmr1=w.KmrWork("./marks.csv",1)
kmr2=w.KmrWork("./marks1.csv",2)
stat = k.Statistic(kmr2)
stat2 = k.Statistic(kmr1)
plot = p.Plots()
plot.set_cat("question_stat")
kmr2.marks_plot(stat.marks_stat())
w.KmrWork.compare_csv()
w.KmrWork.compare_avg_plots(stat.avg_stat(),stat2.avg_stat())
