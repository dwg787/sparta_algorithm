input = "abcba"

def is_palindrome(string):
    for idx in range(len(string)):
        if string[idx] != string[len(string)-1-idx]:
            return False
    return True

print(is_palindrome(input))