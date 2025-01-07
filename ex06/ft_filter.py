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

            print(f"test case {idx}: function={func} | iterable={it}")
            print(f"ft_filter result: {list(ft_filter_result)}")
            print(f"   filter result: {list(filter_result)}\n")

            if idx == 4:
                print("test case 5: checks if iterator is empty")
                print(f"ft_filter result: {list(ft_filter_result)}", end="")
                print(f" | len: {len(list(ft_filter_result))}")
                print(f"   filter result: {list(filter_result)}", end="")
                print(f" | len: {len(list(filter_result))}\n")

    except Exception as e:
        print(f"Exception: an error occurred: {e}")


if __name__ == "__main__":
    main()
