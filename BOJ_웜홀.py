# 벨만-포드
TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())

    edges = []
    for _ in range(M):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    for _ in range(W):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    dist = [0 for _ in range(N+1)]
    def hasCycle():
        for _ in range(N-1):
            for s, e, t in edges:
                dist[e] = min(dist[e], dist[s] + t)

        for s, e, t in edges:
            if dist[e] > dist[s] + t:
                return True
        return False

    print('YES' if hasCycle() else 'NO')