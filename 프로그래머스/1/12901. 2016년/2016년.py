def solution(a, b):
    days = (31,29,31,30,31,30,31,31,30,31,30,31)
    today = ('FRI', 'SAT', 'SUN','MON','TUE','WED','THU')
    
    totalDays = sum(days[:a-1])+(b-1)
    
    return today[totalDays%7]