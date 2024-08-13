def solution(numbers):
    answer = ''
    
    numbers = [str(i) for i in numbers]
    numbers.sort(key = lambda x: x*3, reverse = True)
    answer = str(int(''.join(numbers)))
    
    return answer