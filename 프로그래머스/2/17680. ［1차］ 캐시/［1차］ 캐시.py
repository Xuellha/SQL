def solution(cacheSize, cities):
    answer = 0
    x = []
    for i in range(len(cities)) :   
        a = cities[i].lower()
        if a in x:
            answer += 1   
            x.remove(a)
            x.append(a)
        else :
            answer += 5
            if len(x) == cacheSize :
                x.append(a)
                x.remove(x[0])
            else : 
                x.append(a)  
    return answer