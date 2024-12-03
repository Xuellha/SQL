def solution(order):
    answer = 0
    americano = 0
    latte = 0
    for i in range(len(order)):
        if order[i-1] in ('iceamericano','americanoice','americano','anything','hotamericano','americanohot') :
            americano += 1
        else :
            latte += 1
    answer = americano * 4500 + latte * 5000
    return answer