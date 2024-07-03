def solution(arr, flag):
    x = []
    for i in range(len(flag)):
        if flag[i]:
            x += [arr[i] for x in range(arr[i]*2)]
        else:
            x = x[:len(x)-arr[i]]
    return x