# 최장 증가 수열 응용 (최장 증가 + 최장 감소)
from bisect import bisect_left

N = int(input())
arr = list(map(int, input().split()))

ldp = []
len_ldp = [1 for _ in range(N)]
for i in range(N):
    k = bisect_left(ldp, arr[i])
    if k == len(ldp):
        ldp.append(arr[i])
    else:
        ldp[k] = min(ldp[k], arr[i])

    len_ldp[i] = len(ldp)

rdp = []
len_rdp = [1 for _ in range(N)]
arr.reverse()
for i in range(N):
    k = bisect_left(rdp, arr[i])
    if k == len(rdp):
        rdp.append(arr[i])
    else:
        rdp[k] = min(rdp[k], arr[i])

    len_rdp[N-i-1] = len(rdp)


ans = 0
for i in range(N):
    ans = max(ans, len_ldp[i] + len_rdp[i])
print(ans-1)