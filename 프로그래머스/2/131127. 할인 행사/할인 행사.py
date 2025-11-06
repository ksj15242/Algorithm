def satisfiedWantItems(wantItems, discountItems):
    for item, count in wantItems.items():
        if item not in discountItems or discountItems[item]!=count:
            return False
    
    return True

def solution(want, number, discount):
    n = len(discount)
    wantItems = {k:v for k, v in zip(want, number)}
    
    discountItems = {}
    for item in discount[:10]:
        discountItems[item] = discountItems.get(item, 0) + 1
    
    countDays = 0
    for i in range(n-10):
        if satisfiedWantItems(wantItems, discountItems):
            countDays += 1
        
        discountItems[discount[i]] -= 1
        discountItems[discount[i+10]] = discountItems.get(discount[i+10], 0) + 1
        
    if satisfiedWantItems(wantItems, discountItems):
        countDays += 1    
    
    return countDays