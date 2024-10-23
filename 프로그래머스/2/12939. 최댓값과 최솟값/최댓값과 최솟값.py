def solution(s):
    lis = list(map(int,s.split()))
    lis.sort()
    return str(lis[0])+" "+str(lis[-1])