def solution(rank, attendance):
    filt = [(rank[i],i) for i in range(len(rank)) if attendance[i]]
    filt.sort()
    
    selected_students = [student[1] for student in filt[:3]]
    result = 10000 * selected_students[0] + 100 * selected_students[1] + selected_students[2]
    return result

