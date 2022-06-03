"""
방 생성 조건:
방문했었고 처음 가는 길
"""
from collections import defaultdict


def solution(arrows):
    graph = defaultdict(set)
    dxy = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    def next_pos(p, way):
        d = dxy[way]
        return (p[0] + d[0], p[1] + d[1])

    def oppo_way(way):
        return (way + 4) % 8

    room = 0
    pos = (0, 0)
    for arrow in arrows:
        for _ in range(2):  # 모래시계 케이스를 위해 보폭을 2번
            graph[pos].add(arrow)
            pos = next_pos(pos, arrow)
            # 다음 위치가 (이미 방문됐었고 and 반대 방향으로 찔러지는 선이 없다==처음간다)면 방 생성
            if pos in graph and oppo_way(arrow) not in graph[pos]:
                room += 1
            graph[pos].add(oppo_way(arrow))
    return room


if __name__ == '__main__':
    print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))