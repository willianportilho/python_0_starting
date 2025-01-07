import sys


def check_arguments(args):

    if len(sys.argv) != 3:
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
    word_list: list = text.split(" ")

    return [word for word in word_list if (lambda word: len(word) > number)(word)]


def main():
    try:
        check_arguments(sys.argv[1:])
    except AssertionError as e:
        print(e)
    else:
        print(handle_text(sys.argv[1], int(sys.argv[2])))


if __name__ == "__main__":
    main()
