"""
설치가 안된 곳이 발견 되면
전파의 왼쪽 끝에 닿도록 기지국 설치
"""


# 범위(range) 문제: 끝값만 이용
def solution(n, stations, w):
    now = 1
    i = 0
    answer = 0
    while now <= n:
        if i < len(stations) and stations[i]-w <= now <= stations[i]+w:
            now = stations[i]+w + 1
            i += 1
        else:
            now += 2*w+1
            answer += 1

    return answer


if __name__ == '__main__':
    print(solution(16, [9], 2))