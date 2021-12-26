from collections import defaultdict

if __name__ == '__main__':
    N = int(input())
    cards = list(map(int, input().split()))
    M = int(input())
    wants = list(map(int, input().split()))

    book = defaultdict(int)
    for card in cards:
        book[card] += 1

    for want in wants:
        print(book[want], end=' ')