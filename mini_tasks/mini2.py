def make_pairs(list1, list2):
    pairs = []
    for i in range(min(len(list1), len(list2))):
        pairs.append((list1[i], list2[i]))

    return pairs


# test
a = [1, 2, 3, 100, 1003750102733, 'fuuuuuuuuuu..']
b = ['hello', 'there', 'general', 'ivan']
print(make_pairs(a, b))
