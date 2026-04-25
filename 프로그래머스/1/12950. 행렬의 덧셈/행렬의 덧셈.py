def solution(arr1, arr2):
	return [[a + b for a, b in zip(r1, r2)] for r1, r2 in zip(arr1, arr2)]