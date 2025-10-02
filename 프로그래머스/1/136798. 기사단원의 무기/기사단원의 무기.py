# 숫자를 받아서 약수의 개수를 효율적으로 계산하는 함수
def get_divisor_count(n):
    count = 0
    # 1부터 n의 제곱근까지만 반복
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            # i가 n의 제곱근인 경우 (예: n=16, i=4)
            if i * i == n:
                count += 1
            # 제곱근이 아닌 경우 (예: n=12, i=2 이면 짝인 6도 약수)
            else:
                count += 2
    return count

def solution(number, limit, power):
    total_iron_weight = 0
    
    # 1부터 number까지 각 기사의 약수 개수를 확인
    for knight_number in range(1, number + 1):
        # 효율적인 방법으로 약수 개수(공격력) 구하기
        attack_power = get_divisor_count(knight_number)
        
        # 공격력이 제한수치를 초과하는지 확인
        if attack_power > limit:
            total_iron_weight += power
        else:
            total_iron_weight += attack_power
            
    return total_iron_weight