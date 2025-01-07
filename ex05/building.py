import sys


def count_chars(text: str):
    """
    Counts the number of characters of each type in the given text.

    Parameters:
        text (str): the input text to be analyzed.

    Returns:
        tuple: A tuple containing:
            - text_len (int): Total number of characters in the text.
            - upper (int): Number of uppercase letters.
            - lower (int): Number of lowercase letters.
            - punctuation (int): Number of punctuation marks characters.
            - spaces (int): Number of spaces.
            - digits (int): Number of numeric digits.
    """

    punctuation_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    counts = {
        "text_len": len(text),
        "upper": 0,
        "lower": 0,
        "punctuation": 0,
        "spaces": 0,
        "digits": 0
    }

    for char in text:
        if char.isupper():
            counts["upper"] += 1
        elif char.islower():
            counts["lower"] += 1
        elif char in punctuation_chars:
            counts["punctuation"] += 1
        elif char.isspace():
            counts["spaces"] += 1
        elif char.isdigit():
            counts["digits"] += 1

    return counts


def print_values(values):
    """
    Prints the analysis results of the character counts in a formatted way.

    Parameters:
        values (dict): A dictionary containing the following keys:
            - 'text_len' (int): Total number of characters in the text.
            - 'upper' (int): Number of uppercase letters.
            - 'lower' (int): Number of lowercase letters.
            - 'punctuation' (int): Number of punctuation marks characters.
            - 'spaces' (int): Number of spaces.
            - 'digits' (int): Number of numeric digits.

    Returns:
        None
    """

    print("The text contains", values['text_len'], "characters:")
    print(values['upper'], "upper letters")
    print(values['lower'], "lower letters")
    print(values['punctuation'], "punctuation marks")
    print(values['spaces'], "spaces")
    print(values['digits'], "digits")


def handle_text(text: str):
    """
    Processes the input text by replacing specific unwanted characters
    and calculating the character counts.

    Parameters:
        text (str): The input text to be processed.

    Returns:
        dict: A dictionary containing the following keys:
            - 'text_len' (int): Total number of characters in the text.
            - 'upper' (int): Number of uppercase letters.
            - 'lower' (int): Number of lowercase letters.
            - 'punctuation' (int): Number of punctuation marks characters.
            - 'spaces' (int): Number of spaces.
            - 'digits' (int): Number of numeric digits.
    """

    text = text.replace("\r", " ")
    counts = count_chars(text)
    return counts


def user_input():
    """
    Continuously prompts the user for text input
    until a non-empty string is provided.

    The function reads input line-by-line
    using `sys.stdin.readline` and removes
    a single trailing newline character if present.

    Returns:
        str: The valid input string provided by the user.
    """

    while True:
        print("What is the text to count?")
        user_input = sys.stdin.readline()
        if user_input.endswith("\n"):
            user_input = user_input[:-1]
        if user_input:
            break
    return user_input


def main():
    """
    The main entry point of the program.

    Handles command-line arguments and input text processing:
        - If no arguments are provided or the first argument is empty,
        prompts the user for input.
        - If an argument is provided, uses it as the input text.
        - Validates the number of arguments and raises an AssertionError
        if more than one argument is given.
        - Handles KeyboardInterrupt to terminate the program.

    Returns:
        None
    """

    try:
        if len(sys.argv) > 2:
            raise AssertionError(
                "AssertionError: more than one argument is provided")

        if (len(sys.argv) == 1) or (not sys.argv[1]):
            text: str = user_input()
        else:
            text: str = sys.argv[1]

    except AssertionError as e:
        print(e)
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt: (ctrl + c) was pressed")
    except Exception as e:
        print(f"Exception: an error occurred: {e}")
    else:
        print_values(handle_text(text))


if __name__ == "__main__":
    main()
