class Alphabet:
    lang = "uk"
    letters = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    def __init__(self,lang=lang,letters=letters):
        self.lang=lang
        self.letters=letters

    @classmethod
    def letters_num(cls):
        return len(cls.letters)


    def print_alphabet(self):
        return list(self.letters)

    @classmethod
    def is_ua_lang(cls,text):
        text = text.lower()
        count=0
        for x in text:
            if x in cls.letters:
                count+=1
            else:
                count-=1
        if count ==len(text):
            return "це українська"
        else:
            return "текст містить літери з іншої(их) мов(и)"


class EngAlphabet(Alphabet):
    __en_letters_num=""
    def __init__(self,marking,lang,letters):
        super().__init__(lang,letters)
        self.__en_letters_num=len(letters)
        self.marking=marking

    def letters_num(self):
        return self.__en_letters_num

    @staticmethod
    def example():
        return "Exsample english sentence"

    def is_en_lang(self,text):
        text = text.lower()
        count=0
        for x in text:
            if x in self.letters:
                count+=1
            else:
                count-=1
        if count ==len(text):
            return "is english"
        else:
            return "text contains letters of another language(s)"

