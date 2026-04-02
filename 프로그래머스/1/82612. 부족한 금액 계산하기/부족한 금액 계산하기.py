def solution(price, money, count):
    totalPrice = count*(price+price*count)//2
    
    if totalPrice<=money:
        return 0
    
    return totalPrice-money