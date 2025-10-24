class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    
class EBook(Book):
    def __init__(self,tittle,author,file_size): 
        super().__init__(tittle,author)
        self.file_size=file_size

class PrintBook(Book):        
    def __init__(self,title,author,page_count): 
        super().__init__(title,author)
        self.page_count=page_count
        
class Library:
    def __init__(self):
        self.books=[]
        
    def add_book(self, book):        
        self.books.append(book)
                       
        
    def list_books(self):
    
        for i in self.books:
            if isinstance(i,EBook):
                print( f"EBook: {i.title} by {i.author}, File Size: {i.file_size}KB")
            elif isinstance(i,PrintBook):
                print(f"PrintBook: {i.title} by {i.author}, Page Count: {i.page_count}")
            elif isinstance(i,Book):
                print(f"Book: {i.title} by {i.author}")