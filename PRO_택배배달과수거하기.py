# 그리디 - 먼 집부터 최대로 배달
def solution(cap, n, deliveries, pickups):
    deliveries = [-1] + deliveries
    pickups = [-1] + pickups

    i, j = n, n
    while deliveries[i] == 0:
        i -= 1
    while pickups[j] == 0:
        j -= 1

    arr = []

    def go(k, flag):
        arr = deliveries if flag else pickups

        c = cap
        while k > 0:
            mini = min(arr[k], c)
            c -= mini
            arr[k] -= mini

            if arr[k] != 0:
                break
            k -= 1
        return k

    res = 0
    while i != 0 or j != 0:
        res += max(i, j)
        i = go(i, True)
        j = go(j, False)

    return res * 2
