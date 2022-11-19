# O(n^2*2^n): dis 배열 개수(2**n * n) * 하나 당 최솟값 찾기(n)
if __name__ == '__main__':
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

    dis = [[0 for _ in range(n)] for _ in range(2**n)]
    # dis[s][i] == 현재까지 방문한 집합이 s 이고, 현재 위치한 곳이 i 일때,
    # 아직 방문하지 않은 모든 곳을 방문하고 시작위치(0)로 가는 거리

    # get_dis(10101, 2) == min( graph[2][1] + get_dis(10111, 1), graph[2][3] + get_dis(11101, 3) )
    def get_dis(s, i):
        if dis[s][i] != 0:
            return dis[s][i]

        if s == 2**n - 1:
            d = graph[i][0] if graph[i][0] != 0 else float('inf')
            dis[s][i] = d
            return dis[s][i]

        min_dis = float('inf')
        for j in range(n):
            if i != j and (s & (1 << j)) == 0 and graph[i][j] != 0:
                new_dis = graph[i][j] + get_dis(s | (1 << j), j)
                min_dis = min(min_dis, new_dis)

        dis[s][i] = min_dis
        return dis[s][i]


    print(get_dis(1, 0))

