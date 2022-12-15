# isdigit & isalpha
def solution(files):
    def separ(s):
        a, b = -1, len(s)
        for i in range(len(s)):
            if s[i].isdigit():
                a = i
                break

        for j in range(a, len(s)):
            if not s[j].isdigit() or j - a > 5:
                b = j
                break

        return s[:a].upper(), int(s[a:b])

    files.sort(key=separ)
    return files


if __name__ == '__main__':
    print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))