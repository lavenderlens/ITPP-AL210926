# Q1
class Book:
   def __init__(self, title, author):
         self.title = title
         self.author = author
        #  actual spaces for indent not important
        # but MUST be consistent
   def __str__(self):
        return f"Book title {self.title}, author {self.author}"

book1 = Book("On Liberty", "Mill")
book1.author = "John Stuart Mill"   #setter
print(book1.title)                  #getter
print(book1.author)                 #getter

book2 = Book("The Last Casualty", "Ben Elton")
book2.title = "The First Casualty"
print(book2.title)
print(book2.author)
print(book2)#<__main__.Book object at 0x104f9ca50> WITHOUT __str__
# Book title The First Casualty, author Ben Elton WITH __str__ OVERRIDE

# Q3
class Account:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            
smith = Account("Smith", 12345)
smith.deposit(100)
print(smith.balance)
smith.withdraw(75)
print(smith.balance)
smith.withdraw(50)
print(smith.balance)