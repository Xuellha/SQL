def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)) : 
        if signs[i] == True : 
            s = 1
        else : 
            s = -1
        answer += absolutes[i] * s
    return answer