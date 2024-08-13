def solution(array, commands):
    answer = []
    for i,j in enumerate(commands):
        a = array[j[0]-1:j[1]]
        a = sorted(a)
        answer.append(a[j[2]-1])
    return answer
        