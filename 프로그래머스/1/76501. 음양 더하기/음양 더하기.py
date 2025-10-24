def solution(absolutes, signs):
    sumNumbers = 0
    for num, sign in zip(absolutes, signs):
        if sign:
            sumNumbers += num
        else:
            sumNumbers -= num
    
    return sumNumbers