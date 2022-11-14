array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]

def merge(array1, array2):
    # 이 부분을 채워보세요!
    array_c = []
    arr1_idx = 0
    arr2_idx = 0
    while arr1_idx < len(array1) and arr2_idx < len(array2):
        if array1[arr1_idx] < array2[arr2_idx]:
            array_c.append(array1[arr1_idx])
            arr1_idx += 1
        else:
            array_c.append(array2[arr2_idx])
            arr2_idx += 1
    if arr1_idx == len(array1):
        while arr2_idx < len(array2):
            array_c.append(array2[arr2_idx])
            arr2_idx += 1
    if arr2_idx == len(array2):
        while arr1_idx < len(array1):
            array_c.append(array1[arr1_idx])
            arr1_idx += 1
    return array_c


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!