def solution(people, limit):
    people.sort()
    
    s, e = 0, len(people)-1
    boat = 0
    
    while s<=e:
        weights = people[s]+people[e]
        
        if weights<=limit:
            s += 1
            
        e -= 1
        boat += 1

    return boat