# Shivali Mukherji 
# mukhe105
# CSCI 1133 Section 070
# Assignment 5

import catalog

def get_textbook_price_by_class(class_abbr, class_nbr):

  ''' Gets the price of textbook given a class abbreviation and class number '''

  for cat_info in catalog.catalog:
      if cat_info['abbreviation'] == class_abbr:
          for class_info in cat_info['classes']:
              if class_info['number'] == class_nbr:
                  return class_info['price']
  return 0.00


def get_total_price(class_list):

    '''Takes in a list of class call numbers and outputs the total price of all textbooks in the class list.'''

    total_price = 0.0
    for class_code in class_list:
        class_code_pair = class_code.split()
        #print(class_code_pair[0],class_code_pair[1])
        book_price = get_textbook_price_by_class(class_code_pair[0],class_code_pair[1])
        total_price += book_price
    return total_price

def main():

    '''main function that prints the total textbook price.'''

    my_classes = ["CSCI 1133","CSCI 3081W","CSCI 5511"]
    print(get_total_price(my_classes))


main()
