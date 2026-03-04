from itertools import combinations

def solution(orders, course):
    course_by_len = {n:{} for n in course}
    max_count = {n:0 for n in course}
    
    for order in orders:
        sorted_order = sorted(order)
        
        for k in course:
            if k>len(sorted_order):
                continue
            
            for com in combinations(sorted_order, k):
                key = "".join(com)
                count = course_by_len[k].get(key,0) + 1
                course_by_len[k][key] = count
                
                if count>max_count[k]:
                    max_count[k] = count
    
    answer = []
    for k in course:
        if max_count[k]<2:
            continue
            
        for menu, count in course_by_len[k].items():
            if count==max_count[k]:
                answer.append(menu)
    
    answer.sort()
    
    return answer