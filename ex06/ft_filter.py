def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    try:
        if function is None:
            return iter([item for item in iterable if item])
        else:
            return iter([item for item in iterable if function(item)])
    except Exception as e:
        print(f"Exception: an error occurred: {e}")


def main():
    """Entry point for the program as required by the 42 school rules.

This function does not contain any logic but serves as the standard entry \
point for the script. It is here solely to satisfy the project requirements.

Returns:
    None
    """
    pass


if __name__ == "__main__":
    main()
