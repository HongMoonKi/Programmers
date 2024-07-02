def solution(myString, pat):
    tmp = myString.replace('A', 'C').replace('B', 'A').replace('C', 'B')
    
    return 1 if pat in tmp else 0
