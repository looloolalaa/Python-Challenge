# string handling
from itertools import permutations


def solution(expression):
    temp = expression.replace('*', '-')
    temp = temp.replace('+', '-')
    nums_init = temp.split('-')
    ops_init = [c for c in expression if c == '*' or c == '-' or c == '+']

    op = ['*', '+', '-']
    orders = list(permutations(op, 3))

    result = 0
    for order in orders:
        nums = nums_init[:]
        ops = ops_init[:]
        for o in order:
            while o in ops:
                i = ops.index(o)
                nums[i] = str(eval(nums[i] + o + nums[i + 1]))
                nums.pop(i + 1)
                ops.pop(i)

        result = max(result, (abs(int(nums[0]))))

    return result


if __name__ == '__main__':
    print(solution("100-200*300-500+20"))