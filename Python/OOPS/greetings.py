class Greetings:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def greet(self, fname, lname):
        return f'hello {fname} {lname}'
        
obj = Greetings('A', 'B')
print(obj.greet('Vishnu', 'Vardhan'))