# 구간1: a-b
# 구간2: c-d

# 1. 판별만 하기
# def overlap(a,b,c,d):
#     return a < d and c < b

# 2. 판별과 겹치는 그 구간 구하기
def overlap(a,b,c,d):
    return max(a,c) < min(b,d)
def section(a,b,c,d):
    return [max(a,c), min(b,d)]
