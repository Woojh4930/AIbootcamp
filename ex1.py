def solution(arr):
    k = arr[0]
    answer = [k]
    for i in arr:
        if i != k:
            answer.append(i)
            k = i
            
            
    return answer

"""
def solution(arr):
    answer = [arr[0]]
    for i in arr:
        if answer[-1] != i:
            answer.append(i)
            
            
    return answer
    """