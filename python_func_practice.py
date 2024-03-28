# Write a Python function called max_num()to find the maximum of three numbers.

def max_num(num1, num2, num3):
     if num1 > num2 and num1 > num3:
          return num1
     elif num2 > num1 and num2 > num3:
          return num2
     else:
          return num3
     

print(max_num(10, 20, 30))

# Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(lists):
     result = 1
     for list in lists:
          if isinstance(list, (int, float)):
               result *= list
     return result

print(mult_list([1, 2, 3, 4, 5]))


# Write a Python function called rev_string() to reverse a string.

def  rev_string(s):
     return s[::-1]

print(rev_string("Hello"))


# Write a Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.

def num_within(x, start, end):
     if x in range(start, end+1):
          return True
     else:
          return False

print(num_within(3, 2, 4)) 
print(num_within(3, 1, 3))
print(num_within(10, 2, 5))






# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.

def pascal(n):
     row = [1]
     y = [0]
     for x in range(max(n, 0)):
          print(row)
          row = [left + right for left, right in zip([0] + row, row + [0])]
     return n >= 1

pascal(6)