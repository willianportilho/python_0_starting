def NULL_not_found(object: any) -> int:
    types = [None, 0, False]
    types_str = ["Nothing", "Zero", "Fake"]

    for idx, tp in enumerate(types):
        if (type(object) is type(tp)):
            print(types_str[idx] + ":", object, type(object))
            return (0)

    if (object == ''):
        print("Empty:" + object, type(object))
        return (0)
    elif (object != object):
        print("Cheese:", object, type(object))
        return (0)
    else:
        print("Type not Found")

    return (1)
