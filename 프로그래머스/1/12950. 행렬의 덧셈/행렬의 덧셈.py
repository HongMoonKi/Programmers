def solution(arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        new = [ a+ b for a,b in zip(i,j)]
        answer.append(new)
    return answer
