def solution(array, commands):
    answer = []
    for i in commands:
        array1 = array[i[0]-1:i[1]]
        array1.sort()
        answer.append(array1[i[2]-1])
    return answer