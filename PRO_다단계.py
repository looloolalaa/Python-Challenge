"""
Tree - divide price
"""
from collections import defaultdict


def solution(enroll, referral, seller, amount):
    parent = {}
    for e, r in zip(enroll, referral):
        parent[e] = r

    total = defaultdict(int)

    def divide(name, price):
        if name == '-':
            total['-'] += price
            return
        fee = int(price*0.1)
        take = price - fee
        total[name] += take
        if fee <= 0:
            return
        divide(parent[name], fee)

    for s, a in zip(seller, amount):
        divide(s, 100*a)

    return [total[e] for e in enroll]


if __name__ == '__main__':
    print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))