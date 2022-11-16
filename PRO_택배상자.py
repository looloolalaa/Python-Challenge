# stack
def solution(order):
    container = [i for i in range(len(order), 0, -1)]
    temp = []

    result = 0
    for target in order:
        if not container or target < container[-1]:
            if temp[-1] != target:
                break
            else:
                temp.pop()
                result += 1
        else:
            while container[-1] != target:
                temp.append(container.pop())

            container.pop()
            result += 1

    return result


if __name__ == '__main__':
    print(solution([4, 3, 1, 2, 5]))