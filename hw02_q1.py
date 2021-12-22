# Function to find the sum of numbers
# divisible by 3 in the given range
def sum_thirds(n):
 
    # Variable to store the sum
    sum = 0
 
    # Running a loop from A to B and check
    # if a number is divisible by i.
    for i in range(0, n):
 
        # If the number is divisible,
        # then add it to sum
        if (i % 3 == 0):
            sum += i
 
    # Return the sum
    return sum
   
print(sum_thirds(0))

print(sum_thirds(10))