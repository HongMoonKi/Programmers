def solution(s):
    answer = []
    for i in s:
        if len(answer) == 0:
            answer.append(i)
        elif answer[-1] == "(" and i == ")":
            answer.pop()
        else:
            answer.append(i)
            
    if len(answer) == 0:
        return True
    else:
        return False