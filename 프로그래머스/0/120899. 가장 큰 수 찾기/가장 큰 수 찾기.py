def solution(array):
    array1 = sorted(array, reverse=True)
    a = array.index(array1[0])
    return [array1[0],a]