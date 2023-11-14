# 21억 큰 수 => logn
A, B, C = map(int, input().split())

def f(B):
    if B == 1:
        return A % C

    half = f(B//2) % C
    return half * half % C if B % 2 == 0 else half * half * A % C

print(f(B))