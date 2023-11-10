# 어려운 3진법 (예외)
def solution(n):
    answer = ''
    while n:
        if n % 3 == 0:
            answer += '4'
            n = n//3 - 1
        else:
            answer += str(n % 3)
            n //= 3
    return answer[::-1]
