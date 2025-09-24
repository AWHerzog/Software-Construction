import sys
import json

def do_addieren(args):
    assert len(args) == 2
    left = args[0]
    right = args[1]
    return left + right

def do_absolutewert(args):
    assert len(args) == 1
    value = args[0]
    if value >= 0:
        return value
    return -value

def do_subtrahieren(args):
    assert len(args) == 2
    left = args[0]
    right = args[1]
    return left - right

def do(program):
    if program[0] == "addieren":
        return do_addieren(program[1:])
    if program[0] == "absolutwert":
        return do_absolutewert(program[1:])
    if program[0] == "subtrahieren":
        return do_subtrahieren(program[1:])
    assert False, f"Unkown operation {program[0]}"


def main():
    filename = sys.argv[1]
    with open(filename,'r') as f:
        program = json.load(f)
        result = do(program)
    print(result)

if __name__ == '__main__':
    main()