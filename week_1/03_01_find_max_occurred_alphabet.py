def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26
    alphabet_array = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    max_occurrence = 0
    max_alphabet = alphabet_array[0]
    for alphabet in alphabet_array:
        occurrence = 0
        for char in string:
            if char == alphabet:
                occurrence+=1

        if occurrence > max_occurrence:
            max_occurrence = occurrence
            max_alphabet = alphabet
    # 이 부분을 채워보세요!

    return max_alphabet


print(find_alphabet_occurrence_array("hello my name is sparta"))