# 약수(조건)
def solution(begin, end):
    def maxDivider(n):
        if n == 1:
            return 0

        front = [1]
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                front.append(i)
                rear = n // i
                if rear <= 10_000_000:
                    return rear
        return max(front)

    # begin, end = 100000015, 100000015
    result = []
    for n in range(begin, end+1):
        result.append(maxDivider(n))
    return result