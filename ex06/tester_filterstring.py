import subprocess


GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'


def run_test(input_args, expected_output, expected_error=None):
    """Executes a test by running the script with the provided \
input arguments and checks the output against the expected output and error.

Args:
    input_args (list): A list of input arguments to pass to the script.
    expected_output (str): The expected output from the script.
    expected_error (str, optional): The expected error message \
from the script. Default is None.

Prints:
    - Test results, including success or failure for both output and error.
    - Success messages will be printed in green, while failures will be in red.

This function does not return any value; it only prints the test results.
    """

    result = subprocess.run(
        ["python", "filterstring.py"] + input_args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    output = result.stdout.decode().strip()
    error = result.stderr.decode().strip()

    if output == expected_output:
        print(f"{GREEN}test passed{RESET} with input: {input_args} ", end="")
        print(f"| expexted: {expected_output}")
    else:
        print(f"{RED}test failed{RESET} with input: {input_args} ", end="")
        print(f"| expexted: {expected_output} | got: {output}")

    if expected_error:
        if error:
            if error == expected_error:
                print(f"{GREEN}test passed{RESET} ", end="")
                print("| expected error correctly ", end="")
                print(f"triggered: {expected_error} | input: {input_args}")
            else:
                print(f"{RED}test failed{RESET} ", end="")
                print(f"for input: {input_args} ", end="")
                print(f"| expected error: {expected_error} | got: {error}")
        else:
            print(f"{RED}test failed{RESET} for input: {input_args} ", end="")
            print(f"| expected error: {expected_error}, ", end="")
            print("but no error was raised.")


def test_valid_input():
    """Test case for valid input."""
    run_test(["Hello the World", "4"], "['Hello', 'World']")


def test_large_number_input():
    """Test case for a very large number argument."""
    run_test(['hello the world', '99'], '[]')


def test_invalid_number_of_arguments_input():
    """Test case for invalid number of arguments."""
    run_test(['hello the world', '2', "3"],
             'AssertionError: the arguments are bad')


def test_empty_argument_input():
    """Test case for invalid number of arguments."""
    run_test(['hello the world', '',],
             'AssertionError: the arguments are bad')


def test_wrong_input():
    """Test case for invalid number of arguments."""
    run_test(['3', 'hello the world',],
             'AssertionError: the arguments are bad')


def test_empty_input():
    """Test case for invalid number of arguments."""
    run_test([], 'AssertionError: the arguments are bad')


def main():
    """Main function that runs all the test cases for the script.

This function will:
    - Call each individual test case function (e.g., \
test_valid_input, test_large_number_input)
    - Execute the tests and output the results.

No arguments are passed to this function, and it does not return any value.
The results of the tests are printed directly to the console.

This function serves as the entry point for running the suite of tests.
    """

    test_valid_input()
    test_large_number_input()
    test_invalid_number_of_arguments_input()
    test_empty_argument_input()
    test_wrong_input()
    test_empty_input()


if __name__ == "__main__":
    main()
