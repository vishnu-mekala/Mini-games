#singlelevel_inherit
class Book:
    def __init__(self, title, author, publication, price):
        self.title = title
        self.author = author
        self.publication = publication
        self.price = price
        print('From Book')

class Ebook(Book):
    def __init__(self, title, author, publication, price, format):
        super().__init__(title, author, publication, price)   #
        self.format = format
        print('From Ebook')

obj = Ebook('The Witcher', 'Andrzej Sapkowski', 1986, 251, 'pdf')
