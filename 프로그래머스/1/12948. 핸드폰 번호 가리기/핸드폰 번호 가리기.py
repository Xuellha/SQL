def solution(phone_number):
    x = len(phone_number)-4
    answer = '*' * x + phone_number[x:x+4]
    return answer