def solution(s, n):
    alhpa = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
             's','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k',
             'l','m','n','o','p','q','r','s','t','u','v','w','x','y']
    answer = ""
    s = list(s)
    for i in s:
        result = 0
        if i.isupper():
            i = i.lower()
            result = alhpa.index(i)+n
            answer += alhpa[result].upper()
        elif i.islower():
            result = alhpa.index(i)+n
            answer += alhpa[result]
        else:
            answer = answer+" "
    return answer