class BookShelf():
    
    def __init__(self, name, author, price, published):
        self.book_name = name
        self.book_author = author
        self.book_price = price
        self.book_publish = published
        
    def add_book(self):
        print("Book Name : " + self.book_name)
        print("Book Author : " + self.book_author)
        print("Book Price : " + str(self.book_price) + "/-")
        print("Book Publishing Year : " + str(self.book_publish))
        print("Book Added")
        
    def years_since_publish(self):
        years_ago_pub = 2022 - self.book_publish
        print("This Book Was Published " + str(years_ago_pub) + " Years Ago")
        
book1 = BookShelf("Harry Potter & The Philosopher's Stone", "J.K. Rowling", 1928, 1997)
book1.add_book()
book1.years_since_publish()

book2 = BookShelf("Diary Of A Wimpy Kid", "Jeff Kinney", 700, 2017)
book2.add_book()
book2.years_since_publish()
        

