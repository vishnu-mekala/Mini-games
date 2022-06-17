class Base:
    def m1(self):
        print('this is from base class')

class Derived(Base):
    def m2(self):
        print('this is from derived class')

obj = Derived()
obj.m2()
obj.m1()