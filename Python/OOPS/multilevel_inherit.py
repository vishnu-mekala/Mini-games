class Base:
    def m1(self):
        print('this is from base class')

class Derived(Base):
    def m2(self):
        print('this is from derived class')

class Derived1(Derived):
    def m3(self):
        print('this is from derived1 class')

obj = Derived1()
obj.m3()
obj.m2()
obj.m1()