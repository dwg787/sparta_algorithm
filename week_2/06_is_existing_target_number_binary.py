finding_target = 39
finding_numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

def is_exist_target_number_binary(target, numbers):
    # 이 부분을 채워보세요!
    min_val = finding_numbers[0]
    max_val = finding_numbers[len(finding_numbers)-1]
    guess_val = (min_val+max_val) // 2

    while min_val <= max_val:
        if finding_numbers[guess_val] == target:
            return True
        elif finding_numbers[guess_val] < target:
            min_val = guess_val + 1
        else:
            max_val = guess_val - 1
        guess_val = (min_val + max_val)//2
    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)