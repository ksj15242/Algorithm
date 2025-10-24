def solution(n, lost, reserve):
    lostUniform = set(lost) - set(reserve)
    spareUniform = set(reserve) - set(lost)
    attendStudents = n-len(lostUniform)
    
    for lost in lostUniform:
        if lost-1 in spareUniform:
            spareUniform.remove(lost-1)
            attendStudents += 1
        elif lost+1 in spareUniform:
            spareUniform.remove(lost+1)
            attendStudents += 1
    
    return attendStudents