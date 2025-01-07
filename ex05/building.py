import sys


def count_chars(text: str):
    punctuation_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    text_len: int = len(text)
    upper: int = 0
    lower: int = 0
    punctuation: int = 0
    spaces: int = 0
    digits: int = 0

    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char in punctuation_chars:
            punctuation += 1
        elif char.isspace():
            spaces += 1
        elif char.isdigit():
            digits += 1

    return text_len, upper, lower, punctuation, spaces, digits


def print_values(values):
    print("The text contains", values[0], "characters:")
    print(values[1], "upper letters")
    print(values[2], "lower letters")
    print(values[3], "punctuation marks")
    print(values[4], "spaces")
    print(values[5], "digits")


def handle_text(text: str):
    text.replace("\r", " ")
    values = count_chars(text)
    return values


def user_input():
    while True:
        print("What is the text to count?")
        user_input = sys.stdin.readline()
        if user_input.endswith("\n"):
            user_input = user_input[:-1]
        if user_input:
            break
    return user_input


def main():
    try:
        assert len(sys.argv) < 3, \
            "AssertionError: more than one argument is provided"

        if (len(sys.argv) == 1) or (not sys.argv[1]):
            text: str = user_input()
        else:
            text: str = sys.argv[1]

    except AssertionError as e:
        print(e)
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt: (ctrl + c) was pressed")
    else:
        print_values(handle_text(text))


if __name__ == "__main__":
    main()
