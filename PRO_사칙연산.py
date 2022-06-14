"""
s = [m, M] 최소 최대

괄호 닫는 가짓수
-(a+b + s
1. -(a)+b + s
2. -(a+b) + s
3. -(a+b + s)

=> m = min(-a-b+m, -a-b-M)  : 2, 3 case
   M = max(-a+b+M, -a-b-m)  : 1, 3 case
"""


def solution(arr):
    a, b, s = 0, 0, [0, 0]
    for i in reversed(range(len(arr))):
        if arr[i] != '-' and arr[i] != '+':
            b += int(arr[i])
        if arr[i] == '-':
            a = int(arr[i + 1])
            b -= a
            s = [min(-a - b + s[0], -a - b - s[1]), max(-a + b + s[1], -a - b - s[0])]
            b = 0
    s = [s[0] + b, s[1] + b]
    return s[1]


if __name__ == '__main__':
    print(solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"]))