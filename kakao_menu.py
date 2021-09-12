from itertools import combinations

def solution(orders, course):
    answer = []

    for co in course:
        count={}
        for order in orders:
            comb = combinations(order, co)
            for c in comb:
                key = ''.join(sorted(c))
                if key in count:
                    count[key] += 1
                else:
                    count[key] = 1

        max_count = -1
        if count:
            max_count = max(count.values())
        if max_count>=2:
            for key, value in count.items():
                if value==max_count:
                    answer.append(key)

    answer = sorted(answer)
    return answer


if __name__=='__main__':
    orders = ["XYZ", "XWY", "WXA"]
    course = [2, 3, 4]
    print(solution(orders, course))