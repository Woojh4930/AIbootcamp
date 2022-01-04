<<<<<<< HEAD
def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        arr3 = []    
        for j in range(len(arr1[i])):
            arr3.append(arr1[i][j]+arr2[i][j])
        answer.append(arr3)
    return answer
=======
def solution(seoul):
    answer = f'김서방은 {seoul.index("Kim")}에 있다'
    
    return answer
>>>>>>> 2a0424d9e7dab98c8419b80d756ff2ade09d283d
