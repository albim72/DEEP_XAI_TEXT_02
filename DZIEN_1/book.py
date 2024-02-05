class Book:

    # def __new__(cls, *args, **kwargs):
    #     return object.__new__(Book)

    def __init__(self,id,tytul,autor,cena):
        self.id=id
        self.tytul=tytul
        self.autor=autor
        self.cena=cena
        self.oprawa = "miękka"

    def __repr__(self):
        return f"książka {self.tytul} -> {self.autor}!"


    def print_book(self):
        return (f"książka {self.tytul}, autor: {self.autor}, cena: {self.cena} zl,"
                f" oprawa: {self.oprawa}")

bk = Book(34,"Wiedźmin","Andrzej Sapkowski",40)
print(bk)
bk.oprawa = "twarda"
print(bk.print_book())

bk2 = Book(564,"Hobbit","J.R.R. Tolkien",43)
print(bk2.print_book())
