from math import pi

# Circle "class"
def circle_area(obj):
    return obj["radius"] ** 2 * pi

def circle_perimeter(obj):
    return obj["radius"] * 2 * pi

Circle = {
    "area": circle_area,
    "perimeter": circle_perimeter,
    "_classname": "Circle"
}

def new_circle(name, radius):
    return {
        "name": name,
        "radius": radius,
        "_class": Circle
    }


# Square "class"
def square_area(obj):
    return obj["side"] ** 2

def square_perimeter(obj):
    return obj["side"] * 4

Square = {
    "area": square_area,
    "perimeter": square_perimeter,
    "_classname": "Square"
}

def new_square(name, side):
    return {
        "name": name,
        "side": side,
        "_class": Square
    }


# Polymorphic call
def call(obj, method_name):
    return obj["_class"][method_name](obj)



# Test objects
c1 = new_circle("c1", 10)
c2 = new_circle("c2", 40)
s1 = new_square("s1", 10)
s2 = new_square("s2", 5)

shapes = [c1, c2, s1, s2]

for shape in shapes:
    n = shape["name"]
    a = call(shape, "area")
    p = call(shape, "perimeter")
    c = shape["_class"]["_classname"]
    print(f"{c} {n} has area {a} and perimeter {p}")



