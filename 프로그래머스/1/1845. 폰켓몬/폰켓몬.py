def solution(nums):
    a = len(nums)/2
    if len(set(nums)) >= a:
        return a
    else:
        return len(set(nums))