"""
set() 사용
"""


def solution(skill, skill_trees):

    valid_skill = {''}
    for l in range(len(skill)):
        valid_skill.add(skill[:l+1])

    def removed(s):
        result = ''
        for c in s:
            if c in skill:
                result += c
        return result

    count = 0
    for s in skill_trees:
        s = removed(s)
        if s in valid_skill:
            count += 1


    return count