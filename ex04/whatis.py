import sys

try:
    assert len(sys.argv) > 1, ""
    assert len(sys.argv) < 3, "AssertionError: more than one argument is provided"

    assert len(sys.argv[1]) != 0, "AssertError: no valid input provided, argument is empty"

    user_imput = sys.argv[1]
    if user_imput[0] == '-' or user_imput[0] == '+':
        user_imput = user_imput[1:]
    if not user_imput.isdigit():
        raise AssertionError("AssertionError: argument is not an integer")

    number = int(sys.argv[1])
    assert isinstance(number, int), "AssertionError: argument is not an integer"

    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except AssertionError as e:
    print(e)
