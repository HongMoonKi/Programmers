def solution(s):
    count = 0
    for i in s:
        if i == '(':
            count += 1
        else:
            if count == 0 :
                return False
            else:
                count -= 1
    return count == 0