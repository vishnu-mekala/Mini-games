class Greetings:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def greet(self):
        return f'hello {self.fname} {self.lname}'
        
obj = Greetings('A', 'B')
print(obj.greet())
