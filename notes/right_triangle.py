def is_right_triangle(a,b,c):
    sides = [a,b,c]
    sides.sort()

    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        print("true")
    else:
        print("false")
def area(a,b,c):
    s = (a+b+c)/2
    area = (s* (s-a) * s*(s-b) * s*(s-c))**0.5
    print(area)

side_a = float ( input ("side 1"))
side_b = float ( input ("side 2"))
side_c = float ( input ("side 3"))

