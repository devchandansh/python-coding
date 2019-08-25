
"""
===============================================================
Example-1::
Make Sum or addition of a list items without using the for loop

It is Possible using lambda function, in a Single Line.
===============================================================
"""
from functools import reduce

number_list = [1,2,3,4,5]

# Using the lambda ::
number_sum = reduce((lambda x,y: x+y), number_list )

print("")
print("------------------------------------")
print("Example-1:: list with numbers ")
print("------------------------------------")
print("Default Items are :", number_list)
print("Sum of numbers are :", number_sum)


"""
#output:

------------------------------------
Example-1:: list with numbers
------------------------------------
Default Items are : [1, 2, 3, 4, 5]
Sum of numbers are : 15

"""



"""
===============================================================
Example-2::
Make Sum or addition of a list items without using the for loop
Using Boolean Value as Items
===============================================================
"""

number_list2 = [1,2,3,4,5, True, False]

# Using the lambda ::
number_sum2 = reduce((lambda x,y: x+y), number_list2 )

print("")
print("------------------------------------")
print("Example-2:: list with Boolean Items ")
print("------------------------------------")
print("Default Items are :", number_list2)
print("Sum of numbers are :", number_sum2)


"""
#output:

------------------------------------
Example-2:: list with Boolean Items
------------------------------------
Default Items are : [1, 2, 3, 4, 5, True, False]
Sum of numbers are : 16

"""