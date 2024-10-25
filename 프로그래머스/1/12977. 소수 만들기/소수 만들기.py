def solution(nums):
    answer=[]
    result=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                answer.append(nums[i] + nums[j] + nums[k])
    for b in answer:
        if b > 1:  # 1보다 큰 수만 소수 검사
            is_prime = True
            for i in range(2, int(b**0.5) + 1):
                if b % i == 0:
                    is_prime = False
                    break
            if is_prime:
                result += 1
    return result
            
        