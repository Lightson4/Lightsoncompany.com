'''#1
print("hello worrld")
#2
user_input = input("please enter:")
print(user_input)
#3
num = float(input())
if num > 0:
 print(num, "is positive number")
elif num < 0:
 print(num, "is negetive number")
else:
 print(num, "is zero")

#4
num1 = float(input("Enter the first number"))
num2 = float(input("Enter the second number"))
num3 = float(input("Enter the third number"))
if (num1 >= num3) and (num1 >= num2):
    largest = num1
elif (num2 >= num3) and (num2 >= num1):
    largest = num2
else:
    largest = num3
print(largest)

#5
def factorial(n):
 if n == 0:
  return 1
 else:
  return n * factorial(n-1)
num = int(input("Enter a number: "))
print(f" the factorial id {num} is {factorial(num)}")***
#6
integer_var = 2
float_var = 26.3
string_var = "hello"
boolean_var = True
print(f"integer value: {integer_var}, type: {type(integer_var)}")
print(f"float value: {float_var}, type: {type(float_var)}")
print(f"string value: {string_var}, type: {type(string_var)}")
print(f"boolean: {boolean_var}, type: {type(boolean_var)}")
#7
a =3
b =7
print(f"before swap: a = {a}, b = {b}")
#after swapping
a, b = b, a
print(f"after swapping: a = {a}, b = {b}")
#8 convert celsius to fahrenheit
celsius = float(input("Enter temprature in celsius:"))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}")
#11   arithmatic operations
a = 4
b = 5
add= a + b
print(add)
a = 9
b = 6
div = a * b
print(f"div:", div)

#12comparisam operators
a =5
b =6
print(f"{a} =={b}: {a==b}")
print(f"{a} !={b}: {a!=b}")
print(f"{a} <{b}: {a>b}")
print(f"{a} <{b}: {a<b}")
#13 demostrate logigical operations

a = True
b = False
print(f"True and False: {a and b}")
print(f"not false: {not a}")
#14 squre root of a number
num = float(input("Enter a number: "))
square = num ** 2
print(f"the square of {num} is {square}")

#15 if number is even or odd
num1 = float(input("enter the numnber"))
if num1 % 2 == 0:
    print(f"{num1} is even.")
else:
    print(f"{num1} is odd.")
#17 for calculating leap year
year = int(input("Enter a year:"))
if year % 4 == 0:
     if year % 100 != 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year.")

'''#20 sorting in asending other
numbers = [int(x) for x in input("enter number separated by space:").split()]
numbers.sort()
print(f"sorted list: {numbers}")