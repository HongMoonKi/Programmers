def solution(arr, divisor):
    result = []
    for i in arr:
        if i%divisor== 0:
            result.append(i)
    result.sort()
    return result if len(result) != 0 else [-1]