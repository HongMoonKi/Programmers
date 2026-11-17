def solution(num_str):
    result = 0
    for i in list(num_str):
        result += int(i)
    return result