"""
Stack
"""


def solution(number, k):
    stack = [number[0]]
    for n in number[1:]:
        while stack and stack[-1] < n and k > 0:
            stack.pop()
            k -= 1
        stack.append(n)

    if k > 0:
        stack = stack[:-k]
    return ''.join(stack)


if __name__ == '__main__':
    print(solution("4177252841", 4))