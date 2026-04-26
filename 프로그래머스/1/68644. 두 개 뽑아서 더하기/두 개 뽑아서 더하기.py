from itertools import combinations

def solution(numbers):
    result = []
    for a, b in combinations(numbers, 2):
        result.append(a + b)
    return sorted(set(result))