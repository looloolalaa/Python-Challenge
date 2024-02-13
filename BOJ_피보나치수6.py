# M^n == (M^(n/2))^2
class Mat:
    def __init__(self, mat):
        self.mat = mat

    def __mul__(self, other):
        a, b = self.mat, other.mat
        res = [[0 for _ in range(2)] for _ in range(2)]
        for i in range(2):
            for j in range(2):
                for m in range(2):
                    res[i][j] += a[i][m] * b[m][j]
                    res[i][j] %= mod
        return Mat(res)

def fib(n):
    if n == 1:
        return Mat([[1, 1], [1, 0]])

    half = fib(n // 2)
    if n % 2 == 0:
        return half * half
    else:
        return half * half * fib(1)

mod = 1_000_000_007
n = int(input())
print(fib(n).mat[0][1])

