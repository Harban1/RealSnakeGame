class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def read(self):
        print(f"Reading {self.title} by {self.author}.")

class eBook(Book):
    def __init__(self, title, author, pages, fileSize):
        super().__init__(title, author, pages)
        self.fileSize = fileSize
    
    def download(self):
        print(f"Downloading {self.title}. File size: {self.fileSize} ") 
       
metamorphosis = Book("Metamorphosis", "Franz Kafka", 300)
metamorphosis.read()

lrrh = eBook("Little Red Riding Hood", "Charles Perrault", 10, "50 KB")
lrrh.read()
lrrh.download()