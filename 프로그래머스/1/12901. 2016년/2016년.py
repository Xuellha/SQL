def solution(a, b):
    answer = ''
    num = ''
    week = ['THU','FRI','SAT','SUN', 'MON', 'TUE','WED']
    month_date = [31,29,31,30,31,30,31,31,30,31,30,31]
    num = sum(month_date[:a-1]) + b
    answer = week[num%7]
    return answer