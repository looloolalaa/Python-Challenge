# string slicing & split(' ')
def solution(s):
    def change(word):
        return word[:1].upper() + word[1:].lower()
    return ' '.join([change(w) for w in s.split(' ')])