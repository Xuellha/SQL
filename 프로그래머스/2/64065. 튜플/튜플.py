def solution(s):
    answer = []
    answer1 = []
    s = s[2:len(s)-2]
    s = s.split('},{')
    for i in range(len(s)) : 
        answer.append(s[i].split(','))
    answer.sort(key = len)
    for j in range(len(s)) : 
        for k in range(len(answer[j])) : 
            if answer[j][k] not in answer1 : 
                answer1.append(answer[j][k])
    answer2 = list(map(int, answer1))
    return answer2