# Shivali Mukherji 
# mukhe105
# CSCI 1133 Section 070
# Assignment 5

import catalog

class Book:

    def __init__(self, subject, book_info):

      '''Constructor takes a dictionary object to initialize member values. Subject is a string representing the 3-4 letter department designator eg., CSCI'''

      self.title = book_info['textbook']
      self.price = book_info['price']
      self.class_uses = [subject + ' ' + book_info['number']]

    def book_title(self):
        return self.title

    def book_price(self):
        return self.price

    def book_classes_use(self):
        return self.class_uses


class ShoppingList:
    
    books = []
    
    def __init__(self, courses):

      '''Constructor that takes a list of course designators (eg., "CSCI 1133") and creates a list of Book objects'''

      for class_code in courses:
          class_code_pair = class_code.split()
          subject = class_code_pair[0]
          class_num = class_code_pair[1]
          for course_info in catalog.catalog:
              if course_info['abbreviation'] == subject:
                  for book_infos in course_info['classes']:
                      if book_infos['number'] == class_num:
                          book = Book(subject, book_infos)
                          self.books.append(book)

    def __add__(self, book):
      '''Overload + operator'''
      self.books.append(book)

    def __sub__(self, book):
      '''Overload - operator'''
      if len(self.books) > 0:
          self.books.remove(book)


    def get_total_price(self):
      '''Return total price.'''
      total_price = 0.0
      for book in self.books:
          total_price += book.book_price()
      return total_price


def main():

    '''main function that prints the total textbook price.'''

    class_list = ["CSCI 1133","CSCI 3081W","CSCI 5511"]
    shop_list = ShoppingList(class_list)
    print(shop_list.get_total_price())



main()