def create_reversed_dict(src_dict):
    reversed_dict = dict()
    to_repeat = set()
    for value_new, key_new in src_dict.items():
        if key_new in reversed_dict and key_new not in to_repeat:
            reversed_dict[key_new] = (reversed_dict[key_new],)
            to_repeat.add(key_new)
        if key_new in to_repeat:
            reversed_dict[key_new] += value_new,
        else:
            reversed_dict[key_new] = value_new

    return reversed_dict


# test
d = {"Ivanov": 97832, "Petrov": 55521, "Kuznetsov": 97832, "Kenobi": 97832, "General": 55521}
# if we include in our set something like []: "lol", or "kek": [] TypeError must occur (I tried)
reversed_d = create_reversed_dict(d)
print(reversed_d)
