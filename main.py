import sys
points = int(input("how many points does your shape have?: "))
dilate_operations = ["*", "x", "dilate", "times", "multiply", "grow", "expand", "contract", "shrink"]
x_points = []
y_points = []
x_prime = []
y_prime = []
current_point = 0
def dilate(list, factor, satic):
    if str(type(list)) != "<class 'list'>":
        sys.stderr.write("\n in 'dilate()' function, first argument must be a list. instead it received" + str(type(list)) + "\n")

    if str(type(factor)) != "<class 'float'>" and str(type(factor)) != "<class 'int'>":
        sys.stderr.write("\n in 'dilate()' function, second argument must be a int or float. instead it received" + str(type(factor)) + "\n")

    if str(type(static)) != "<class 'float'>" and str(type(factor)) != "<class 'int'>":
        sys.stderr.write("\n in 'dilate()' function, third argument must be a int or float. instead it received" + str(type(factor)) + "\n")

        index = 0
        while True:
            index += 1
            list[index] = (list[index] * factor) + static
            if index >= len(list):
                break

while True:
    new_x = float(input("Enter X coordinate of point" + str(current_point + 1) + ": " ))
    x_points.append(new_x)
    new_y = float(input("Enter Y coordinate of point" + str(current_point + 1) + ": " ))
    y_points.append(new_y)
    if current_point < points - 1:
        current_point += 1
    else:
        break
operation = input("enter an operation or transformation type 'none' to quit: ")
operation = operation.lower()
if operation in dilate_operations:
    sf = float(input("input a scale factors: "))
    staticx = float(input("input X coordinate center of dilation: "))
    staticy = float(input("input Y coordinate center of dilation: "))
    dilate(x_points, sf, staticx)
    dilate(y_points, sf, staticy)
