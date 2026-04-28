def solution(s):
    answer = []
    answer.append(s[0])
    for i in range(1,len(s)):
        if answer and s[i] == ")" and answer[-1] == "(":
            answer.pop()
        else:
            answer.append(s[i])
    return True if len(answer)==0 else False