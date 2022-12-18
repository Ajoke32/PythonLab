class Buffer:
    __numbers_list=[]  #список для зберігання результатів суми
    __num_fives=[] #список для того, щоб працювати з вхідними даними
    def __init__(self):#ініаліція
        pass #пропускаємо
    @classmethod
    def add(cls,*nums): #метод додавання числа
       for i in nums: #цикл по доданим числам
           cls.__num_fives.append(i) #запис в лист всіх значень
           if len(cls.__num_fives)%5==0: #якщо довжина листа кратна 5
                cls.__numbers_list.append(sum(cls.__num_fives[0:5])) #в лист сум заносимо суму першої пятірки
                cls.__num_fives=cls.__num_fives[5:len(cls.__num_fives)] #в листі, де всі значення, залишаємо лише ті
                #що не були додані в основний масив сум


    @classmethod
    def get_current_part(cls): #поточний буфер
        return cls.__numbers_list+cls.__num_fives #список з сумами та список з елементами, які не утворюють пятірку
