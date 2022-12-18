class Apple:
    states=["Відсутнє","Цвітіння","Зелене","Червоне"]

    def __init__(self,index):
        self._index=index
        self._state=self.states[0]

    def grow(self):
        if self._state!=self.states[3]:
            self._state=self.states[self.states.index(self._state)+1]
            return True
        else:
            return False

    def is_ripe(self):
        if self._state==self.states[3]:
            return True
        else:
            return False


class AppleTree:
    def __init__(self,amount):
        self.amont=amount
        self.appels=[]
        self.make_list()


    def make_list(self):
        for x in range(0,self.amont):
            self.appels.append(Apple(x))

    def grow_all(self):
        for x in self.appels:
            if not x.grow():
                return False
        return True

    def all_are_ripe(self):
        for x in self.appels:
            if not x.is_ripe():
                return False

        return True

    def give_away_all(self):
        self.appels=[]


class Gardener:
    def __init__(self,name,tree):
        self.name=name
        self._tree=tree

    def work(self):
        if not self._tree.grow_all():
            print("Працювати не можу, всі яблука  достигли, час збирати урожай")

    def harvest(self):
        if self._tree.all_are_ripe():
            self._tree.give_away_all()
            print("Урожай зібрано")
        else:
            print("Яблука ще не дозріли")

    def apple_base(self):
        for x in self._tree.appels:
            print(F"apple {x._index} {x._state}")
