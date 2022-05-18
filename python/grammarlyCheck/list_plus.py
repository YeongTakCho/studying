list1 = [[1, 2], [2, 3]]
list2 = [[3, 4], [5, 6]]
nlist = tuple(list1)+tuple(list2)
print(set(list(map(tuple, list1+list2))))
