import function1_data
'''
#definding a function or creating a function
def Student ():
'''
#functions without parameters 
def Greet ():
    print("hello, welcome to AWT academy")
Greet()


def weeks ():
    print("there are 7 days ina week")
weeks()
#functions with parameters
def square(numbers):
    return numbers ** 2
results= square(numbers=5)
print(results)
#functions with multiple parameters
def rectangle_area (length,width):
    return length*width
area = rectangle_area(5,9)
print(f"The area of the reactangle is {area}")
'''
'''# functions with Multiple parameters
def arithematic (a , b):
    return a-b, a+b, a/b, a*b, a%b
result1 = arithematic(7,9)
print(result1)
#class work on same with multiple parameters
def calculate_average (courses):
    return  sum(courses)/len(courses)
courses = [80,90,75, 85, 95, 65, 78]
average = calculate_average(courses)
print(f"Average: {average}")

#another one
def school (gruop):
    return school("acts, science")
    student = school("43, 32")
print(school)
#one example
def even_odd (num):
    if num%2 == 0:
        print("the number is even")
    else:
        print("the number is odd")
even_odd(18)
function1_data.result()