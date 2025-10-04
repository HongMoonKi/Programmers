def solution(wallet, bill):
    result = 0
    while max(bill) > max(wallet) or min(bill) > min(wallet):
        if bill[0] > bill[1]:
            bill[0] = bill[0]//2
            result+=1
        else:
            bill[1] = bill[1]//2
            result+=1
    return result