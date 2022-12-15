if __name__ == '__main__':
    # 알파벳 내림차순, 만약 같다면 길이로 정렬
    temp = ['abc', 'bc', 'ca', 'ca', 'D', 'da', 'asdasd']

    # 순서 반대!!!!
    temp.sort(key=lambda x: len(x))
    temp.sort(key=lambda x: x, reverse=True)
    print(temp)


