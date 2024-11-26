def solution(arr):
    answer = arr.copy()
    if len(arr) == 1:
        return [-1]
    arr.sort(reverse=True)
    x = arr.pop()
    answer.remove(x)
    return answer