from collections import Counter

def solution(clothes):
    count = Counter([i[1] for i in clothes])

    result = 1
    for v in count.values():
        result *= (v + 1)

    return result - 1