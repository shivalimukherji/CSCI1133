# Shivali Mukherji
# mukhe105
# CSCI 1133 Section 070
# Assignment 4

def get_nth_generalized_fibonacci_number(n, *args):

  '''converts the arbitrary sequence to a list, and uses recursion to compute numbers in a fibonacci sequence.'''

  alist = list(args)
  nlist = [int(elm) for elm in alist]

  def get_nth_fibonacci_list(n, nlist):
    if n <= 0:
      return 0
    elif n == 1:
      return 1
    else:
      # Return sum(f(n-1), f(n- 2) and so on...)
      return sum(get_nth_fibonacci_list(n - k, nlist) for k in nlist)

  return (get_nth_fibonacci_list(n, nlist))


if __name__ == "__main__":
  #Running example 1 --> compute f1,2(n) pass 1 and 2 as arguments after n.
    print('Running example with n --> 1 thru 6, with tuple -> (1,2)')
    print(get_nth_generalized_fibonacci_number(1,1,2))
    print(get_nth_generalized_fibonacci_number(2,1,2))
    print(get_nth_generalized_fibonacci_number(3,1,2))
    print(get_nth_generalized_fibonacci_number(4,1,2))
    print(get_nth_generalized_fibonacci_number(5,1,2))
    print(get_nth_generalized_fibonacci_number(6,1,2))

  #Running example 2 --> compute f1,2,3(n) pass 1,2 and 3 as arguments after n.
    print('Running example with n --> 1 thru 6, with tuple -> (1,2,3)')
    print(get_nth_generalized_fibonacci_number(1,1,2,3))
    print(get_nth_generalized_fibonacci_number(2,1,2,3))
    print(get_nth_generalized_fibonacci_number(3,1,2,3))
    print(get_nth_generalized_fibonacci_number(4,1,2,3))
    print(get_nth_generalized_fibonacci_number(5,1,2,3))
    print(get_nth_generalized_fibonacci_number(6,1,2,3))

  #Running example 3 --> Negative values for n and zero are special cases
    print('Running example with n --> 0 and -3, with tuple -> (1,2)')
    print(get_nth_generalized_fibonacci_number(0,1,2))
    print(get_nth_generalized_fibonacci_number(-3,1,2))
  