def solution(arr):
    x = []
    
    for i in arr:
        x.extend([i]*i)
    return x