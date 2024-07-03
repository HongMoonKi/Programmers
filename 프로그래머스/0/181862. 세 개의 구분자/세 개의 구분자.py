def solution(myStr):
    myStr1 = myStr.replace('a'," ").replace('b'," ").replace('c'," ")
    
    myStr2 = myStr1.split()
    
    return myStr2 or ["EMPTY"]
    