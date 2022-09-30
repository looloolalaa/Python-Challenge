# double.isInteger
def solution(n):
    sqrt = n ** 0.5
    if sqrt % 1 == 0:
        return (sqrt+1)**2
    return -1


if __name__ == '__main__':
    print(solution(121))