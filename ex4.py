<<<<<<< HEAD
def solution(n):
    answer = 0

    for i in str(n):
        answer+=int(i)

=======
def solution(s):
    answer = ''
    a = list(str(s))
    if len(a)%2 ==1:
        answer = a[len(a)//2]
    else:
        answer=a[len(a)//2-1]+a[len(a)//2]
>>>>>>> 2a0424d9e7dab98c8419b80d756ff2ade09d283d
    return answer