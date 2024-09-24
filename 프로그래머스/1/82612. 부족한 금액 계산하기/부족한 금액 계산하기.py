def solution(price, money, count):
    a = 1
    result = 0
    while a <= count:
        result += price*a
        a += 1
        
    if result >= money:
        return result - money
    else:
        return 0