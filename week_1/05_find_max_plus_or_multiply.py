# input = [0, 3, 5, 6, 1, 2, 4]
# input = [3,2,1,5,9,7,4]
input = [1,1,1,3,3,2,5]

def find_max_plus_or_multiply(array):
    # 이 부분을 채워보세요!
    cal_result = array[0]
    for idx, val in enumerate(array):
        if idx == 0:
            continue
        elif cal_result+array[idx] > cal_result*array[idx]:
            cal_result = cal_result+array[idx]
        elif cal_result+array[idx] < cal_result*array[idx]:
            cal_result = cal_result*array[idx]

    return cal_result

result = find_max_plus_or_multiply(input)
print(result)

# 모범답안

# def find_max_plus_or_multiply(array):
#     multiply_sum = 0
#     for number in array:
#         if number <= 1 or multiply_sum <= 1:
#             multiply_sum += number
#         else:
#             multiply_sum *= number
#     return multiply_sum