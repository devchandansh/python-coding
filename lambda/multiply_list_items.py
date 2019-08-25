
"""
===============================================================
Make Square of a list items without using the for loop

It is Possible using lambda function, in a Single Line.
===============================================================
"""

number_list = [1,2,3,4,5]

# Using the lambda ::
number_squares = list(map( (lambda x: x*2), number_list ))


print("Default Items are :", number_list)
print("Square of numbers are :", number_squares)


"""
#output:

Default Items are : [1, 2, 3, 4, 5]
Square of numbers are : [2, 4, 6, 8, 10]

"""
