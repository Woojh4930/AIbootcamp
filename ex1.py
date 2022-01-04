<<<<<<< HEAD
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
=======
def solution(a, b):
    answer = 0
    for i in range(min(a,b),max(a,b)+1):
        answer += i
    return answer
>>>>>>> 2a0424d9e7dab98c8419b80d756ff2ade09d283d
