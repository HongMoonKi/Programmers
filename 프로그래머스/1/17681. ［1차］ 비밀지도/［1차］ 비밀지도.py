def solution(n, arr1, arr2):
    a, b = [], []
    answer = []

    for i in range(n):
        a.append(bin(arr1[i])[2:].zfill(n))
        b.append(bin(arr2[i])[2:].zfill(n))

    for j, k in zip(a, b):
        row = ''
        for z in range(n):
            if j[z] == "0" and k[z] == "0":
                row += " "
            else:
                row += "#"
        answer.append(row)

    return answer