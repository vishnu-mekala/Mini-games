#polymorphism
#an object showing diff states in diff stages of its life cycle.
#two types
#dynamic poly ex: method overiding
#static poly ex: method overloading (not possible)

class Parents:

    def marry(self):
        print('Katherine')

class Child(Parents):
    def marry(self):
        print('Langford')

obj = Child()
obj.marry()