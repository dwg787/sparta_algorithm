input = "abadabac"

def find_not_repeating_character(string):
    alphabet_occurrence_array = [0] * 26
    alphabet_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z']
    # 이 부분을 채워보세요!
    for el in string:
        if el.isalpha():
            arr_idx = ord(el)-ord('a')
            alphabet_occurrence_array[arr_idx] += 1

    not_repeating_character_arr = []
    for idx in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[idx]
        if alphabet_occurrence == 1:
            not_repeating_character_arr.append(chr(idx + ord('a')))

    for char in string:
        if char in not_repeating_character_arr:
            return char

result = find_not_repeating_character(input)
print(result)