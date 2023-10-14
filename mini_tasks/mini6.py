def flatten(src_list):
    dst_list = []
    for elem in src_list:
        if isinstance(elem, list):
            dst_list += flatten(elem)
        else:
            dst_list.append(elem)
    return dst_list


print(flatten([1, 2, [3, [4, 5], 6], [7, [8, [9]]]]))
