def flip_parentheses(u):
    return ''.join('(' if c == ')' else ')' for c in u)

def is_correct_parentheses(u):
    stack = 0
    
    for c in u:
        if c=='(':
            stack += 1
        else:
            stack -= 1
        
        if stack<0:
            return False
    
    return stack==0
            
def split_parentheses(w):
    stack = 0
    
    for i, c in enumerate(w):
        if c=='(':
            stack += 1
        else:
            stack -= 1
        
        if stack==0:
            return w[:i+1], w[i+1:]
    
    return w, ''

def convert_parentheses(w):
    if w=='':
        return ''
    
    u, v = split_parentheses(w)
    
    if is_correct_parentheses(u):
        return u + convert_parentheses(v)
    
    return  '(' + convert_parentheses(v) + ')' + flip_parentheses(u[1:-1])
    
def solution(p):
    return convert_parentheses(p)