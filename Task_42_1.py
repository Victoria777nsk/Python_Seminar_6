def check_sorted(somelist):
    if sorted(set(somelist)) == somelist:
        return 1
    elif sorted(set(somelist), reverse = True) == somelist:
        return -1
    return 0
s_dict = {
    1: 'Возрастает',
    -1: 'Убывает',
    0: 'Ни то, ни то'
            }

print(s_dict[check_sorted([1, 2, 3])])
print(s_dict[check_sorted([3, 2, 3])])
print(s_dict[check_sorted([3, 2, 1])])
print(check_sorted([1, 1, 2, 3]))