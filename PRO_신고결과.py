from collections import defaultdict


def solution(id_list, report, k):
    reported = defaultdict(set)
    report_count = defaultdict(int)

    for s in set(report):
        a, b = s.split()
        reported[a].add(b)
        report_count[b] += 1

    return [len(list(filter(lambda x: report_count[x] >= k, reported[i]))) for i in id_list]


if __name__ == '__main__':
    print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))