# Shivali Mukherji
# mukhe105
# CSCI 1133 Section 070
# Assignment 4

def check_rec_lower_given_threshold(numbers, threshold):

  '''recieves a list of ints and an int that represents a threshold as parameters. returns a list of boolean values in which the value is true if the respective number is lower than the threshold, or returns false if otherwise.'''


  def recurse(numbers, threshold):
    '''since recursion has to happen inside, an inner private function was defined to do the recursion.'''

    if len(numbers) == 0:
      return []
    else: 
      tmplist = []
      if numbers[0] < threshold:
        tmplist.append(True)
      else:
        tmplist.append(False)
    return tmplist + recurse(numbers[1:], threshold)
   # Print the list of booleans
  print(recurse(numbers, threshold))

def main():
  check_rec_lower_given_threshold([1, 2, 3, 4, 5, 6, 1, 3], 4)
  check_rec_lower_given_threshold([1,2],4)
  check_rec_lower_given_threshold([],0)

main()
  
  