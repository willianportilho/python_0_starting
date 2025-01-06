def all_thing_is_obj(object: any) -> int:
    obj_types = [list, tuple, set, dict]
    str_types = ["List", "Tuple", "Set", "Dict"]

    for idx, tp in enumerate(obj_types):
        if (type(object) is tp):
            print(str_types[idx], ":", type(object))
            return (42)

    if (type(object) is str):
        if ((object == "Brian") | (object == "Toto")):
            print(object, "is in the kitchen :", type(object))
    else:
        print("Type not found")

    return (42)
