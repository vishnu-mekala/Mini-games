class Base:
    m1 = 'from base1'

class Derived1(Base):
    pass

class Derived2(Base):
    pass

obj = Derived1()
print(obj.m1)
obj = Derived2()
print(obj.m1)