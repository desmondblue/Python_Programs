class Book:
    
    def __init__(self,t,a,p):
        self.title = t
        self.author = a
        self.publisher_info = p
    def display(self):
        return self.title,self.author,self.publisher_info
a = Book("Sherlock Holmes","Sir Arthur Conan Doyle","Penguin Books")
b = a.display()
print(b)