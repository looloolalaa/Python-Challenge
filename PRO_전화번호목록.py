"""
set check: phone[:1~n-1]
"""


def solution(phone_book):
    book = set(phone_book)

    def sub_str(s):
        result = []
        for l in range(1, len(s)):
            result.append(s[:l])
        return result

    for phone in phone_book:
        for s in sub_str(phone):
            if s in book:
                return False
    return True


if __name__ == '__main__':
    print(solution(["119", "97674223", "1195524421"]))