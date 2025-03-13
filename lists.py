# # Write a Python function to reverse a list at a specific location.

# def reverse_list(my_list, start, end):  

#     # Reverse the sublist
#     start, end = end, start

#     my_list[start, end]
#     print(my_list)



mlist = [1,2,3,4,5,78]

# # reverse_list(mlist, 3, 6) 

# def sum_of_list(mlist):
#     return sum(mlist)


# print(sum_of_list(mlist))

# def multiply_list(mlist):
#     result = 1

#     for item in mlist:
#         result *= item
#     print(result)

# multiply_list(mlist)


# def max_num(mlist):
#     return max(mlist)

# print(max_num(mlist))

# import math
# import os
# import random
# import re
# import sys



# if __name__ == '__main__':
#     n = int(input().strip())
#     if n % 2 != 0:
#         print("Weird")
#     elif n % 2 == 0:
#         if n >= 2 and n <= 5:
#             print("Not Weird")
#         elif n >= 6 and n <= 20:
#             print("Weird")
#         elif n > 20:
#             print("Not Weird")

# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
    
#     total = a + b
#     sub = a - b
#     product = a * b
    
# print(total, sub, product)

courses = ["Math", "Physics", "CompSci", "Art"]

course = "Art" 

print(courses.index(course),  course)

course_str = ', '.join(courses)
print(course_str)

print(course_str.split(","))