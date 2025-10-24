def solution(bandage, health, attacks):
    castTime, regenPerSec, bonusRegen = bandage
    maxHealth = health
    pastAttackTime = 0
    
    for attackTime, damage in attacks:
        healTime = attackTime-pastAttackTime-1
        totalHeal = (healTime//castTime)*bonusRegen + healTime*regenPerSec
        health = min(maxHealth, health+totalHeal)
        
        health -= damage
        pastAttackTime = attackTime
        
        if health<=0:
            return -1
        
    return health