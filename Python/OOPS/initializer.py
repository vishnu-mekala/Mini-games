class Init:
    def __init__(self, x):  # x is local variable
        print('This runs everytime we create an object')
        n = 10  # local varaible/attributes
        self.x = x # self.x is instance variable

obj1 = Init(10) # It will run the __init__()
obj2 = Init(20)
obj3 = Init(30)
obj4 = Init(40)
obj5 = Init(50)
