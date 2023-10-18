def flatten(src_list, depth=float("inf")):  # float("itf") классная вещь, все-таки
    """
    This function returns flattened to some depth list.
    :param src_list: input list
    :param depth: depth, to what we want to flatten list
    :return: flattened list
    """
    dst_list = []
    for elem in src_list:
        if isinstance(elem, list) and depth > 0:
            dst_list += flatten(elem, depth=depth - 1)
        else:
            dst_list.append(elem)
    return dst_list


exp1 = [1, 2, [3, [4, 5], 6], [7, [8, [9]]]]
print(flatten(exp1, depth=1))
print(flatten(exp1, depth=2))
print(flatten(exp1))

exp2 = [1, [2, [3, [4, [5, [6, [7, [8, [9]]]]]]]]]
print(flatten(exp2, depth=5))
