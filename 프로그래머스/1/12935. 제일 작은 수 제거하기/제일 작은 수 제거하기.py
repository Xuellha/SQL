def solution(arr):
    answer = []
    for i in range(len(arr)) : 
        if i == 0 :
            x = arr[i]
        else : 
            if arr[i] < x : 
                x = arr[i]
    arr.remove(x)          
    if len(arr)== 0 : 
        answer.append(-1)
    else : 
        answer = arr
       
    return answer