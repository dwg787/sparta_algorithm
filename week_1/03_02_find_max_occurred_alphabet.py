def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for el in string:
        if el.isalpha():
            arr_idx = ord(el) - ord('a')
            alphabet_occurrence_array[arr_idx]+=1

    max_occurrence = 0
    max_alphabet_idx = 0
    for idx in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[idx]
        if alphabet_occurrence > max_occurrence:
            max_alphabet_idx = idx
            max_occurrence = alphabet_occurrence

    return chr(max_alphabet_idx + ord('a'))


print(find_alphabet_occurrence_array("hello my name is sparta"))