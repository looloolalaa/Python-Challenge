# 2개 점 선택후 정사각형 만들기
from itertools import combinations
import sys
input = sys.stdin.readline

def get_rect(p1, p2):
    dx, dy = p2[0]-p1[0], p2[1]-p1[1]

    dx, dy = dy, -dx
    p3 = p2[0]+dx, p2[1]+dy

    dx, dy = dy, -dx
    p4 = p3[0]+dx, p3[1]+dy

    return [p3, p4]

T = int(input())
for _ in range(T):
    N = int(input())
    visited = set()
    points = []
    for _ in range(N):
        a, b = map(int, input().split())
        points.append((a, b))
        visited.add((a, b))

    ans = 0
    for p1, p2 in combinations(points, 2):
        p3, p4 = get_rect(p1, p2)
        if p3 in visited and p4 in visited:
            ans = max(ans, (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
    print(ans)