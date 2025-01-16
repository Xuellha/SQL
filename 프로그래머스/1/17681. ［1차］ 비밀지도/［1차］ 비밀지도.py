# def solution(n, arr1, arr2):
#     answer = []
#     for i in range(n) : 
#         for j in range(n) : 
#             if bin(arr1[i])[2:].zfill(n)[j] == '1' or bin(arr2[i])[2:].zfill(n)[j] == '1' :
#                 answer[i] = str(answer[i]) + '#'
#             else : 
#                 answer[i] = str(answer[i]) + ' '
#     return answer

# def solution(n, arr1, arr2):
#     answer = ['' for _ in range(n)]
#     for i in range(n) :
#         arr1[i] = bin(arr1[i])[2:].zfill(n)
#         arr2[i] = bin(arr2[i])[2:].zfill(n)
#     for i in range(n) : 
#         for j in range(n) :  
#             if arr1[i][j] == '1' or arr2[i][j] == '1' : 
#                 answer[i][j] += '#'
#             else : 
#                 answer[i][j] += ' '
#     return answer  

def solution(n, arr1, arr2):
    answer = ['' for _ in range(n)]
    for i in range(n):
        arr1[i] = bin(arr1[i])[2:].zfill(n)
        arr2[i] = bin(arr2[i])[2:].zfill(n)
    for i in range(n):
        for j in range(n):
            if arr1[i][j] == '1' or arr2[i][j] == '1': 
                answer[i] += '#' 
            else:
                answer[i] += ' ' 
    return answer

        