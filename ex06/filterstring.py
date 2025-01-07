import sys


def check_arguments(args):
    """Validates the arguments passed to the script.

This function checks if the arguments passed to the script are:
    - Exactly two arguments.
    - The first argument (text) contains only \
alphanumeric characters and spaces.
    - The second argument (number) is a valid integer (positive or negative).

Args:
    args (list): The list of arguments passed to the script.

Raises:
    AssertionError: If any of the validation checks fail.
    """

    if (not args[0]) or (not args[1]):
        raise AssertionError(
            "AssertionError: the arguments are bad")

    text = args[0]
    if any((not char.isalnum()) and (not char.isspace())
           for char in text):
        raise AssertionError(
            "AssertionError: the arguments are bad")

    number = args[1]
    try:
        if (number[0] == '-') or (number[0] == '+'):
            number = number[1:]
        if not number.isdigit():
            raise AssertionError(
                "AssertionError: the arguments are bad")
    except ValueError:
        raise AssertionError(
            "AssertionError: the arguments are bad")


def handle_text(text: str, number: int):
    """Filters words from the text that have more \
than a specified number of characters.

This function splits the input text into words \
and returns a list of words whose \
length is greater than the specified number.

Args:
    text (str): The input text to be filtered.
    number (int): The minimum length of the words to keep.

Returns:
    list: A list of words with a length greater than the specified number.
    """

    word_list: list = text.split(" ")

    return [word for word in word_list
            if (lambda word: len(word) > number)(word)]


def main():
    """Main entry point of the script.

This function:
    - Checks if the arguments passed to the script \
are valid using `check_arguments`.
    - Calls `handle_text` to filter words from the input text \
that are longer than the specified length.
    - Prints the resulting filtered list of words.

Returns:
    None
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError(
                "AssertionError: the arguments are bad")

        check_arguments(sys.argv[1:])
    except AssertionError as e:
        print(e)
    else:
        print(handle_text(sys.argv[1], int(sys.argv[2])))


if __name__ == "__main__":
    main()
