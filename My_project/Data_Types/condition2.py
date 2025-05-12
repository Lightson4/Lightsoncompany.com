import function1_data
def traffic_light (color):
    if color == "red":
        return "stop"
    elif color == "yellow":
        return "caution"
    elif color == "green":
        return "go"
    elif color == "black":
        return "night"
    else:
        return "unexpected color"
color= input("enter traffic color(red, yellow, green, black):")
print(traffic_light(color))
function1_data.Greet()