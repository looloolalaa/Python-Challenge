def move(n, start, end, temp):
    if n <= 1:
        print(start+'->'+end)
        return
    move(n-1, start, temp, end)
    move(1, start, end, temp)
    move(n-1, temp, end, start)


if __name__ == '__main__':
    move(10, 'A', 'C', 'B')