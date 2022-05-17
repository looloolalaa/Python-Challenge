"""
A: 0->n-1 오른쪽으로 한번에 가는 경우
B: min(front로 갔다가 왼쪽으로 돌아서 rear, rear로 돌아서 갔다가 다시 front)
answer: min(A, B)
"""


def solution(name):
    move = 0

    have_to_go = []
    for i, c in enumerate(name):
        if c != 'A':
            have_to_go.append(i)
            front = ord(c) - ord('A')
            rear = ord('Z') - ord(c) + 1
            move += min(front, rear)

    def get_min_dis():
        if not have_to_go:
            return 0
        elif len(have_to_go) == 1:
            return min(have_to_go[0], len(name)-have_to_go[0])

        min_dis = have_to_go[-1]
        for i in range(len(have_to_go)-1):
            front, rear = have_to_go[i], len(name) - have_to_go[i+1]
            new_dis = min(2*front+rear, 2*rear+front)
            min_dis = min(min_dis, new_dis)
        return min_dis

    return move + get_min_dis()


if __name__ == '__main__':
    print(solution("BBABAAAB"))