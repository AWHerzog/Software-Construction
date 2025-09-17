a = [1, 2, 3]

def example():
    print("in example")

def example2():
    print("in example2")

list_of_functions = [example, example2]

for f in list_of_functions:
    f()