from itertools import combinations
def solution(numbers):
    result = []
    for num in combinations(numbers, 2):
        result.append(sum(num))
    return sorted(set(result))