def solution(my_string):
    owl = ['a', 'e', 'i', 'o', 'u' ]
    answer = ''
    for i in my_string:
        if i not in owl:
            answer += i
    return answer