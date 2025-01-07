from ft_filter import ft_filter


def main():
    """Main function that runs multiple test cases to compare the results \
of the custom filter function `ft_filter` \
and the built-in `filter` function.

The function:
    - Defines a list of test cases with different functions and iterables.
    - Iterates over each test case, applying both \
`ft_filter` and `filter` to the iterable.
    - Compares the results of both functions \
and prints the output for each test case.
    - Specifically checks an edge case where the iterator is empty.

Returns:
    None
    """

    try:
        test_cases = [
            (None, [0, None, 1, 2, ""]),
            (lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            (lambda x: x.upper(), ["Python", "Language"]),
            (lambda x: len(x) > 3, ["Hello", "my", "Brazil!"])
        ]

        for idx, (func, it) in enumerate(test_cases, start=1):
            ft_filter_result = ft_filter(func, it)
            filter_result = filter(func, it)

            print(f"test case {idx}: iterable={it}")
            print(f"ft_filter result: {list(ft_filter_result)}")
            print(f"   filter result: {list(filter_result)}\n")

            if idx == 4:
                print("\ntest case 5: checks if iterator is empty")
                print(f"ft_filter result: {list(ft_filter_result)}", end="")
                print(f" | len: {len(list(ft_filter_result))}")
                print(f"   filter result: {list(filter_result)}", end="")
                print(f" | len: {len(list(filter_result))}\n")

        print("test case 6: compares __doc__")
        print("the documentations (__doc__) are equal!"
              if ft_filter.__doc__ == filter.__doc__ else
              "the documentations (__doc__) are different!")

        print("\ntest case 7: prints ft_filter.__doc__")
        print(ft_filter.__doc__)

    except Exception as e:
        print(f"Exception: an error occurred: {e}")


if __name__ == "__main__":
    main()
