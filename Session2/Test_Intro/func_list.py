
def first():
    print("first")

def second():
    print("second")

def third():
    print("third")

everything = [first, second, third]

for each_func in everything:
    each_func()