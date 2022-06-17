class Base1:
    m1 = 'base1'

class Base2:
    m1 = 'base2'

class Derived(Base2, Base1):
    pass

obj = Derived()
print(obj.m1)