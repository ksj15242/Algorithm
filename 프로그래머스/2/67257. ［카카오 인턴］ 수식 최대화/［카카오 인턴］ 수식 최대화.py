from itertools import permutations

def parse_expression(expression):
    finds = ('-', '*', '+')
    
    operators = set()
    result = []
    
    num = ''
    for c in expression:
        if c in finds:
            result.append(int(num))
            result.append(c)
            operators.add(c)
            num = ''
        else:
            num += c
    
    result.append(int(num))
    
    return result, operators

def solution(expression):
    answer = 0
    
    calc = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b
    }
    parsed_expression, operators = parse_expression(expression)
    
    for priority in permutations(operators):
        after = parsed_expression[:]
        
        for op in priority:
            before = after
            after = [before[0]]
            
            i = 1
            while i<len(before):
                if before[i]==op:
                    after.append(calc[op](after.pop(), before[i+1]))
                else:
                    after.append(before[i])
                    after.append(before[i+1])
                
                i += 2
                    
        answer = max(answer, abs(after[0]))
        
    return answer