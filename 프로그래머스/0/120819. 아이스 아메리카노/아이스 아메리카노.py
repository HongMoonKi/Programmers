def solution(money):
    answer = 0
    while money >= 5500:
        answer += 1
        money = money - 5500
    return [answer,money]