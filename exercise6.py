# Exercise 6: Find the Largest Number
#
# Write a function named `largest` that takes three integers as arguments and returns the largest of them.
#
# Examples:
# largest(1, 2, 3) should return 3.
# largest(10, 4, 2) should return 10.
#
# Define your function and test it with different inputs.
def largest (a, b, c):
    if a > b and a > c:
        return a 
    elif b > a and b > c:
        return b 
    elif c > b and c > a:
        return c 
    


print('Exercise 6:', largest(1, 2, 3))
