if __name__ == '__main__':
    n = 144
    print(bin(n)[2:])
    print(oct(n))
    print(hex(n))

    # 2,8,16 X -> have to make func
    def n_radix(n, k):
        answer = ''
        while n:
            answer += str(n % k)
            n //= k
        return answer[::-1]

    print(n_radix(n, 3))

    # n진수 -> 10진수
    print(int(n_radix(n, 3), 3))
    # int == 10진수
