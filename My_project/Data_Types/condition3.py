import function_data
#credit system
name = input("Please what is your name:")
def calculate_grade (score):
    try:
         
    # this is a nested conditional statement
         if score >= 100:
              print(f" Hey, {name} there is a miscalculation in your Score")   
         elif score >= 80 and score <= 100:
             return "A"
         elif score >= 70 and score <= 79:
            return "AB"
         elif score >= 65 and score <= 69:
            return "B"
         elif score >= 60 and score <= 64:
            return "BC"
         elif score >= 50 and score <= 59:
            return "C"
         elif score >= 40 and score <= 49:
            return "D"
         elif score >= 30 and score <= 39:
            return "E"
         else:
            "F"
    
    except TypeError:
                print("Invalid score")
try:
    score = int(input("please enter your score:"))
    print(f" hey, {name} Your grade is: {calculate_grade(score)}.")
except ValueError:
    print("Invalid score")
function_data()