input = [4, 6, 2, 9, 1]

def insertion_sort(array):
    # 이 부분을 채워보세요!
    n = len(array)
    for i in range(1, n):
        for j in range(i):
            print(i, j)
            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]
            else:
                break
    return

insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!