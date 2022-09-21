# define a function for calculating
# the area of a shapes
def calculate_area(name): \
        # converting all characters
    # into lower cases
    name = name.lower()

    # check for the conditions
    if name == "rectangle":
        l = int(input("Enter rectangle's length: "))
        w = int(input("Enter rectangle's width: "))

        # calculate area of rectangle
        rect_area = l * w
        print("The area of rectangle is: " + str(rect_area))

    elif name == "square":
        s = int(input("Enter square's side length: "))

        # calculate area of square
        sqt_area = s * s
        print("The area of square is " + str(sqt_area))

    elif name == "triangle":
        h = int(input("Enter triangle's height length: "))
        w = int(input("Enter triangle's width length: "))

        # calculate area of triangle
        tri_area = 0.5 * w * h
        print("The area of triangle is: " + str(tri_area))

    elif name == "circle":
        r = int(input("Enter circle's radius length: "))
        pi = 3.14

        # calculate area of circle
        circ_area = pi * r * r
        print("The area of circle is" + str(circ_area))

    else:
        print("Sorry! This shape is not available")

        # driver code
if __name__ == "__main__":
    print("Calculate Shape Area")
    shape_name = input("Enter the name of shape whose area you want to find: ")

    # function calling
    calculate_area(shape_name)