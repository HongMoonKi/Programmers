def solution(arr):
    stk = []
    i = 0
    while i < len(arr) :
        if stk != [] and stk[-1] == arr[i] :
            del stk[-1]
            i += 1
        else :
            stk.append(arr[i])
            i += 1
    return stk or [-1]
    
