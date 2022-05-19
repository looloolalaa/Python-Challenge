"""
제일 끝에 카메라를 설치하고 겹치면 노카운트
안 겹치면 새 카메라 설치
"""


def solution(routes):
    routes.sort(key=lambda x: x[1])

    count = 1
    camera = routes[0][1]
    for route in routes[1:]:
        start, end = route
        if start > camera:
            count += 1
            camera = end
    return count


if __name__ == '__main__':
    print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))