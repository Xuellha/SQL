def solution(nums):
    answer = 0
    x = []
    for i in range(len(nums)) : 
        if nums[i] not in x : 
            x.append(nums[i])  
    if len(x) > len(nums)/2 : 
        answer = len(nums)/2
    else :
        answer = len(x)
    return answer