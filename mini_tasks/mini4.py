def create_reversed_dict(src_dict):
    reversed_dict = {}

    for value_new, key_new in src_dict.items():
        if key_new in reversed_dict:
            if isinstance(reversed_dict[key_new], tuple):
                reversed_dict[key_new] += value_new,  # append tuple if exists with 'value_new,' (one-element tuple)
            else:
                reversed_dict[key_new] = (reversed_dict[key_new], value_new)  # create tuple if not exists
        else:
            reversed_dict[key_new] = value_new  # just create new element by key_new

    return reversed_dict


# test
d = {"Ivanov": 97832, "Petrov": 55521, "Kuznetsov": 97832, "Kenobi": 97832, "General": 55521}
# if we include in our set something like []: "lol", or "kek": [] TypeError must occur (I tried)
reversed_d = create_reversed_dict(d)
print(reversed_d)
