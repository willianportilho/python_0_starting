import sys


def handle_text(text):
    print("'" + text + "'")


def user_input():
    while True:
        user_input = input("What is the text to count?\n")
        if user_input:
            break
    return user_input


def main():
    try:
        assert len(sys.argv) < 3, \
            "AssertionError: more than one argument is provided"

        if (len(sys.argv) == 1) or (not sys.argv[1]):
            text = user_input()
        else:
            text = sys.argv[1]

    except AssertionError as e:
        print(e)
    except EOFError:
        print("EOFError: (ctrl + d) was pressed")
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt: (ctrl + c) was pressed")
    else:
        handle_text(text)



if __name__ == "__main__":
    main()
