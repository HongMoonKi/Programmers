def solution(a, b):
    days = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    months = [31,29,31,30,31,30,31,31,30,31,30,31]
    
    total_days = sum(months[:a-1]) + b - 1
    
    return days[total_days % 7]