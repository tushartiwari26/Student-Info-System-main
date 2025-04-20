
class Library:
    def __init__(self):
        self.noBooks=0
        self.books=[]
    def addBook(self,book):
        self.books.append(book)
        self.noBooks=len(self.books)
    def show(self,book):
        print(f"The library has {self.noBooks}books.The books are")  
        for book in self.books:
            print(books)


l1=Library()
l1.addBook("Sahil Maurya")
l1.showInfo()



























