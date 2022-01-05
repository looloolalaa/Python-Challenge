if __name__ == '__main__':
    temp = [1,2,3,4,5,6,7,8,9,4444,4444,1,1,4,5,6,7,4444]

    max_val = -float('inf')
    max_indices = []
    for i, num in enumerate(temp):
        if num > max_val:
            max_val = num
            max_indices = [i]
        elif num == max_val:
            max_indices.append(i)

    print(max_val, max_indices)
    print(temp.count(max(temp)))