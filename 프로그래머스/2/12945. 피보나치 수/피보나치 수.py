def solution(n):
    answer = 0
    if n >= 2 : 
        x = 0
        y = 1
        for i in range(n-1) :
            answer = x + y 
            x = y
            y = answer
        answer = answer % 1234567
    elif n == 1 : 
        answer = 1 % 1234567
    else :
        answer = 0 % 1234567
    return answer