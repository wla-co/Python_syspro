def cycle(iterable, el_count):
    i = 0
    while el_count > 0:
        if i > len(iterable) - 1:
            i = 0
        yield iterable[i]
        i += 1
        el_count -= 1


def chain(*iterables):
    for iterable in iterables:
        for el in iterable:
            yield el


my_list = [42, 13, 7]
print(list(chain([1, 2, 3], ['a', 'b'], my_list)))

print(list(cycle([1, 2, 3], 10)))
