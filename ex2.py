<<<<<<< HEAD
a, b = map(int, input().strip().split(' '))


print(("*"*a+"\n")*b)
=======
def solution(n):
    answer = ''
    for i in range(n):
        if i%2 == 0:
            answer += "수"
        else:
            answer += "박"
    return answer

solution(2)
>>>>>>> 2a0424d9e7dab98c8419b80d756ff2ade09d283d
