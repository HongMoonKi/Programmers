def solution(number,limit,power):  
    result = []
    real = 0
    for i in range(1,number+1):
        answer = 0
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                if j == i // j:
                    answer += 1
                else:
                    answer += 2
        result.append(answer)
    for k in result:
        if k <= limit:
            real += k
        else:
            real += power
    return real
                