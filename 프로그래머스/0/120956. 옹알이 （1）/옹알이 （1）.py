def solution(babbling):
    answer = 0
    bab = ["aya", "ye", "woo", "ma"]

    for word in babbling:
        for sound in bab:
            word = word.replace(sound, " ")

        if word.replace(" ", "") == "":
            answer += 1

    return answer