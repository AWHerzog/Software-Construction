import pprint

def sign(value):
    if value < 0:
        return -1
    else:
        return 1
    
def test_sign_negative():
    expected = -1
    result = sign(-3)
    assert result == expected

def test_sign_positive():
    expected = 1
    result = sign(3)
    assert result == expected



def run_tests():
    test_results = {"passed": 0, "failed": 0, "errors": 0}

    for (name, test) in globals().items():
        if not name.startswith("test_"):
            continue
        try:
            test()
            test_results["passed"] += 1
        except AssertionError:
            test_results["failed"] += 1
        except Exception:
            test_results["errors"] += 1
    print(f"passed: {test_results['passed']}, failed: {test_results['failed']}, errors: {test_results['errors']}")


#tests = [test_sign_negative, test_sign_positive]
#run_tests(tests)



#def find_tests(prefix="test_"):
#    for (name, func) in globals().items():
#        if name.startswith(prefix):
#            print(name)
#find_tests()

run_tests()