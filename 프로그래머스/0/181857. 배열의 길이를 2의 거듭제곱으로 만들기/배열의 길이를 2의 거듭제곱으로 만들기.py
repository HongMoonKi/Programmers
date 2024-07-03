def solution(arr):
    i = 0 
    while len(arr) > 2**i:
        i += 1
    zero = 2**i - len(arr)
    zero1 = [0]*zero
    
    
    return arr + zero1