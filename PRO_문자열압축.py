# [i:i+spl]
def solution(s):
    lens = []
    for spl in range(1, len(s) + 1):
        candi = [s[i:i + spl] for i in range(0, len(s), spl)]

        res = ''
        now = ''
        count = 1
        for c in candi + ['']:
            if c == now:
                count += 1
            else:
                res += (str(count) if count > 1 else '') + str(now)
                now = c
                count = 1

        lens.append(len(res))

    return min(lens)
