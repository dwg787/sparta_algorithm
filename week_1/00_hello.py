input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    new_val = array[0]
    for el in array:
        if el >= new_val:
            new_val = el
    return new_val

result = find_max_num(input)
print(result)