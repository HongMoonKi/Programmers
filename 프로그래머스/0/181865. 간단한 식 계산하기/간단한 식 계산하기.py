def solution(binomial):
    
    x = binomial.split()
    
    if x[1] == '+':
        return int(x[0])+int(x[2])
    elif x[1] == '-':
        return int(x[0])-int(x[2])
    elif x[1] == '*':
        return int(x[0])*int(x[2])