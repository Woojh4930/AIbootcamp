def solution(n, m):
    answer = []
    
    a,b = n,m
    while True:
        if a%b == 0:
            answer.append(b)
            answer.append(n*m//b)
            break
        a,b = b,a%b
    
    return answer