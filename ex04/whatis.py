import sys

try:
    assert len(sys.argv) > 1, ""
    assert len(sys.argv) < 3, "AssertionError: more than one argument is provided"

    assert len(sys.argv[1]) != 0, "AssertError: no valid input provided, argument is empty"

    number = int(sys.argv[1])
    assert isinstance(number, int), "AssertionError: argument is not an integer"

    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except AssertionError as e:
    print(e)
except ValueError as e:
    print("AssertionError: argument is not an integer")
