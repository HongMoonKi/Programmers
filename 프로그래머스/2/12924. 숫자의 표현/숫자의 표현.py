def solution(num):
    answer = 0
    for i in range(1, num+1):
        add = 0
        while add <= num:
            add += i
            i += 1
            if add == num:
                answer += 1
    return answer