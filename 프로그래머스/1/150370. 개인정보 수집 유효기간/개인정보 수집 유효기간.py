def dateToDay(date):
    year, month, day = map(int, date.split("."))
    
    return 12*28*year+28*month+day

def solution(today, terms, privacies):
    termMap = {}
    for term in terms:
        code, exp = term.split(" ")
        termMap[code] = int(exp)*28
        
    todayDate = dateToDay(today)
    rmList = []
    for i, privacy in enumerate(privacies):
        date, code = privacy.split(" ")
        privacyDate = dateToDay(date)+termMap[code]-1
        
        if todayDate>privacyDate:
            rmList.append(i+1)
        
    return rmList