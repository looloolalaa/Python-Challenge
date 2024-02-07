# look and say algorithm
# 배열에서 연속된 값의 개수 세기
def get_sequence(arr):
    result = []
    i = 0
    while i < len(arr):
        count = 1
        while i < len(arr) - 1 and arr[i] == arr[i + 1]:
            i += 1
            count += 1
        result.append([arr[i], count])
        i += 1
    return result


print(get_sequence([1,2,3,3,4,4,4,4,4,2,0,0]))