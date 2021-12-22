# Shivali Mukherji
# mukhe105
# CSCI 1133 Section 070
# Assignment 3

def maximum_product(list1, list2):

  '''Takes two list inputs of integers and returns the product of the two largest elements.'''

  # condition with loop that multiplies that the largest integer from each list
  if len(list1) == 0 or len(list2) == 0:
    return 'None'
  else:
    prodlist = []
    for i in list1:
      for j in list2:
        prodlist.append(i*j)
    return max(prodlist)

# driver function
def main():

    '''Tests the list inputs so that the maximum product can be determined.'''

    max_product = maximum_product([],[1,2,3])
    print(max_product)

    max_product = maximum_product([3,4,5,1,2],[1,2,3])
    print(max_product)

    max_product = maximum_product([-2,-5,1],[-2,-3,4,2])
    print(max_product)

main()
