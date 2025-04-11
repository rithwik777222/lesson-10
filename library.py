class library:
    def __init__(self,list_of_books,name):
        self.bookslist = list_of_books
        self.name = name
        self.lenddict = {}

    def displaybooks(self):
      print("the books available in our library are: {self.name}")
      for book in self.bookslist :
        print(book)

    def lendbook(self,user,book):
     if book not  in self.lenddict:
        print('sorry we do not have the book')
     elif book in self.lenddict:
        print('the book has been borrowed by {self.lenddict[book]}')
     else:
        self.lenddict[book] = user
        print("book data base has been updted.you can now take yor book.")

    def addbook(self,book):
     self.bookslist.append(book)
     print(book,"has been aded to the list")

    def returnbook(self,book):
     if book in self.lenddict:
      del self.lenddict[book]
      print('book has been returned')
     else:
      print("that book was not borroed from us")

if __name__ == '__main__'
  books = library(['python','wonka','harry potter','planet of apes','html'],"let's upskill")
  user_name = input('welcome to our library')
