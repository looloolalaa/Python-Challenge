# string sequence
def solution(skill, skill_trees):
    valid = {skill[:l] for l in range(len(skill) + 1)}

    def is_valid(s):
        s = ''.join([c for c in s if c in skill])
        return s in valid

    result = 0
    for s in skill_trees:
        if is_valid(s):
            result += 1
    return result


if __name__ == '__main__':
    print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))