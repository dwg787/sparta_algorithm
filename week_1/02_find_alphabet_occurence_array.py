def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for el in string:
        if el.isalpha():
            arr_idx = ord(el) - ord('a')
            alphabet_occurrence_array[arr_idx]+=1

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))