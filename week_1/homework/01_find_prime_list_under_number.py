input = 20

def find_prime_list_under_number(number):
    # 이 부분을 채워보세요!
    new_arr = []
    for num in range(2, number+1):
        for num2 in range(2, num):
            if num % num2 == 0:
                break
        else: #break이 걸리지 않았다면
            new_arr.append(num)
    return new_arr

result = find_prime_list_under_number(input)
print(result)