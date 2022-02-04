from collections import defaultdict

def last_point(v):
    dic_x = defaultdict(int)
    dic_y = defaultdict(int)
    for v in v:
        dic_x[v[0]] += 1
        dic_y[v[1]] += 1

    answer = []
    for k, v in dic_x.items():
        if v==1:
            answer.append(k)
    for k, v in dic_y.items():
        if v==1:
            answer.append(k)
    return answer


if __name__ == '__main__':
    V = [[1, 10], [1, 1], [4, 1]]
    print(last_point(V))


