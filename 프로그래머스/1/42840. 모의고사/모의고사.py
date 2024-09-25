def solution(answers):
    
    man1 = [1,2,3,4,5]
    man2 = [2,1,2,3,2,4,2,5]
    man3 = [3,3,1,1,2,2,4,4,5,5]
    
    score = [0,0,0]
    result = []
    
    for idx, answer in enumerate(answers):
    	if answer == man1[idx%len(man1)]:
        	score[0] += 1
    	if answer == man2[idx%len(man2)]:
        	score[1] += 1
    	if answer == man3[idx%len(man3)]:
        	score[2] += 1   
    for idx, s in enumerate(score):
    	if s == max(score):
        	result.append(idx+1)
    return result