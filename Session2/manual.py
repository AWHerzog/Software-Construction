
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

tests = [test_sign_negative, test_sign_positive]

def run_tests(all_tests):
    test_results = {"passed": 0, "failed": 0, "errors": 0}

    for test in all_tests:
        try:
            test()
            test_results["passed"] += 1
        except AssertionError:
            test_results["failed"] += 1
        except Exception:
            test_results["errors"] += 1
    print(f"passed: {test_results['passed']}, failed: {test_results['failed']}, errors: {test_results['errors']}")

run_tests(tests)