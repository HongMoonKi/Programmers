import itertools

def solution(number):
    result = 0
    answer = list(itertools.combinations(number,3))
    for i in answer:
        a = sum(i)
        if a == 0:
            result += 1
    return result