def solution(s, n):
    t = ''
    for i in s : 
        if i.islower() : 
            t = t + chr((ord(i) - ord('a') + n) % 26 + ord('a'))
        elif i.isupper() : 
            t = t + chr((ord(i) - ord('A') + n) % 26 + ord('A'))
        else : 
            t = t + i
    return t