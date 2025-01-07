def solution(s, n):
    answer = ''
    # A=65 Z=90 a=97 z=122 공백=32
    # 대문자 65~90 소문자 97~122
    s = list(s)
    ord_list = []
    for i in s:
        ord_list.append(ord(i))
        to_chr_list = [] # 다시 알파벳으로 바꿔야하는 아스키코드값 리스트
        for ordnum in ord_list:
            if ordnum == 32:
                pass
            # 대문자인 경우
            elif 65 <= ordnum <= 90:
                ordnum = (ordnum-65+n)%26 + 65
            # 소문자인 경우
            elif 97 <= ordnum+n <= 122:
                ordnum = (ordnum-97+n)%26 + 97
            else:
                ordnum += (n-26)
            to_chr_list.append(ordnum)
    for to_chr in to_chr_list:
        new_alpha = chr(to_chr)
        answer += new_alpha
    return answer