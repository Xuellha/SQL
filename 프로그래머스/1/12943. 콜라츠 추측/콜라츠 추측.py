def solution(num):
    answer = 0
    for i in range(500) : 
        if num != 1 :  
            if num % 2 ==0 : 
                num = num / 2
            else :
                num = num * 3 + 1
            answer += 1
        else : 
            break
    if num != 1 : 
        answer = -1     
        
    return answer