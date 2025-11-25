def solution(phone_book):
    n = len(phone_book)
    phone_book.sort()
    
    for i in range(n-1):
        prefix = phone_book[i]
        m = len(prefix)
        
        if prefix==phone_book[i+1][:m]:
            return False
    
    return True