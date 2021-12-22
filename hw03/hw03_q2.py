# Shivali Mukherji
# mukhe105
# CSCI 1133 Section 070
# Assignment 3

def check_diagonal(mat):
  
  '''Takes a matrix input and checks if it has a diagonal or not. The matrix must be a square matrix.'''

  n = len(mat)
  for i in range(0, n):
    for j in range(0, n):
       # condition to check other elements except main diagonal are zero or not. 
      if i != j and mat[i][j] != 0:
         return False
  return True

# driver function
def main():

    '''Tests these square matrix inputs in order to determine whether each of them have diagonals or not.'''

    result = check_diagonal([[1,0,0],[0,1,0],[0,0,1]])
    print(result)

    result = check_diagonal([[1,0,0],[0,2,0],[3,0,1]])
    print(result)

    result = check_diagonal([[1,0,0,0],[0,2,0,2],[3,0,1,0],[3,1,1,2]])
    print(result)

    result = check_diagonal([[1,0,0,0],[0,2,0,0],[0,0,3,0],[0,0,0,4]])
    print(result)
   
main()


      