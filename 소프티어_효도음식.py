# 구간합의 최댓값 dp - O(N)
n = int(input())
arr = list(map(int, input().split()))

ldp = [-1 for _ in range(n)]
ldp[0] = arr[0]
for i in range(1, n):
    ldp[i] = max(ldp[i-1]+arr[i], arr[i])

rdp = [-1 for _ in range(n)]
rdp[n-1] = arr[n-1]
for i in range(n-2, -1, -1):
    rdp[i] = max(rdp[i+1]+arr[i], arr[i])

lsdp = ldp[:]
for i in range(1, n):
    lsdp[i] = max(lsdp[i], lsdp[i-1])

rsdp = rdp[:]
for i in range(n-2, -1, -1):
    rsdp[i] = max(rsdp[i], rsdp[i+1])

ans = -float('inf')
for i in range(1, n-1):
    ans = max(ans, lsdp[i-1] + rsdp[i+1])
print(ans)
