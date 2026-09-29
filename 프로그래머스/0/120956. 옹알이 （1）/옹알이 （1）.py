def solution(babbling):
    answer = 0
    sound = ["aya", "ye", "woo", "ma"]

    for i in babbling:
        for j in sound:
            i = i.replace(j, " ")
            
        if i.replace(" ", "") == "":
            answer += 1      
    return answer