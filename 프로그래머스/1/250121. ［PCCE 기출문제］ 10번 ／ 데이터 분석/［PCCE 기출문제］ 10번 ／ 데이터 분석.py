def solution(data, ext, val_ext, sort_by):
    element = {"code":0, "date":1, "maximum":2, "remain":3}
    
    processedData = []
    for raw in data:
        if raw[element[ext]]<val_ext:
            processedData.append(raw)
    
    processedData.sort(key=lambda x : x[element[sort_by]])
        
    return processedData
