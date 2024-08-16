def solution(players, callings):
    rank =  {key : i for i, key in enumerate(players)}

    for calling in callings:
        index = rank[calling]
        rank[calling] -= 1 # 추월한 선수
        rank[players[index - 1]] += 1 # 추월당한 선수
        players[index - 1], players[index] = players[index], players[index - 1]

    return players