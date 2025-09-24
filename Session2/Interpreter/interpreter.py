import sys
import json
import pprint

def do_set(args, env):
    assert len(args) == 2
    assert isinstance(args[0], str)
    var_name = args[0]
    var_value = do(args[1], env)
    env[var_name] = var_value
    return var_value

def do_get(args, env):
    assert len(args) == 1
    assert isinstance(args[0], str)
    assert args[0] in env, f"unknown variable {args[0]}"
    return env[args[0]]
    

def do_seq(args, env):
    for each_ops in args:
        res = do(each_ops, env)
    return res

def do_addieren(args, env):
    assert len(args) == 2
    left = do(args[0], env)
    right = do(args[1], env)
    return left + right

def do_absolutewert(args, env):
    assert len(args) == 1
    value = do(args[0], env)
    if value >= 0:
        return value
    return -value

def do_subtrahieren(args, env):
    assert len(args) == 2
    left = do(args[0], env)
    right = do(args[1], env)
    return left - right

def do(program, env):
    if isinstance(program, int):
        return program



    if program[0] == "addieren":
        return do_addieren(program[1:], env)
    if program[0] == "absolutwert":
        return do_absolutewert(program[1:], env)
    if program[0] == "subtrahieren":
        return do_subtrahieren(program[1:], env)
    if program[0] == "seq":
        return do_seq(program[1:], env)
    if program[0] == "set":
        return do_set(program[1:], env)
    if program[0] == "get":
        return do_get(program[1:], env)
    assert False, f"Unkown operation {program[0]}"


def main():
    filename = sys.argv[1]
    with open(filename,'r') as f:
        program = json.load(f)
        env = dict()
        result = do(program, env)
    print(">>>", result)
    pprint.pprint(env)

if __name__ == '__main__':
    main()