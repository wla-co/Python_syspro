def specialize(fun, *args, **kwargs):
    def part_fun(*add_args, **add_kwargs):
        return fun(*args, *add_args, **kwargs, **add_kwargs)

    return part_fun


def sum(x, y):
    return x + y


plus_one = specialize(sum, y=1)
just_two = specialize(sum, 1, 1)

print(plus_one(10))  # 11
print(just_two())  # 2
