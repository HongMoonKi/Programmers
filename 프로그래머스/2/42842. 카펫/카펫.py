def solution(brown, yellow):
    answer = []
    total = brown+yellow

    for i in range(1,total+1):
        if total%i == 0:
            w = total//i
            h = i
            if (w - 2) * (h - 2) == yellow:
                return [w,h]