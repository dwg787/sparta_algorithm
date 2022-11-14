s = "(())()"
# stack으로 푸는 문제

def is_correct_parenthesis(string):
    stack = []

    for idx in range(len(string)):
        if string[idx] == '(':
            stack.append(string[idx])
        elif string[idx] == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    if len(stack) != 0:
        return False
    else:
        return True


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!