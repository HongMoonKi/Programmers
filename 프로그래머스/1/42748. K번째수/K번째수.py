def solution(array, commands):
    answer = []
    for i in commands:
        a = sorted(array[i[0]-1:i[1]])
        b = a[i[2]-1]
        answer.append(b)
    return answer