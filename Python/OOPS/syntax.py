#class declare
class ClassName:
    attributes1 = 145
    attributes2 = 17

    def method(self):
        print('in method', self)

#object

obj = ClassName()
print(obj)
print(obj.attributes1)
print(obj.attributes2)
obj.method()