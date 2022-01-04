<<<<<<< HEAD
def solution(n, m):
    answer = []
    
    a,b = n,m
    while True:
        if a%b == 0:
            answer.append(b)
            answer.append(n*m//b)
            break
        a,b = b,a%b
    
=======
def solution(x, n):
    answer = [x*i for i in range(1,n+1)]
>>>>>>> 2a0424d9e7dab98c8419b80d756ff2ade09d283d
    return answer