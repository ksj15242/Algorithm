def solution(keymap, targets):
    keyIndex = {}
    for keys in keymap:
        for i, key in enumerate(keys):
            keyIndex[key] = min(i+1, keyIndex.get(key, 101))
    
    minPressCount = [0]*len(targets)
    for i, target in enumerate(targets):
        for c in target:
            if c not in keyIndex:
                minPressCount[i] = -1
                break
            
            minPressCount[i] += keyIndex[c]
    
    return minPressCount