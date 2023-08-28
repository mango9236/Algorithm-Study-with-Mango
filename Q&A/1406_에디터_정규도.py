import sys
left=list(sys.stdin.readline().strip('\n'))
right=[]
n=int(sys.stdin.readline())

for i in range(n):
    command=input().split()
    if command[0]=="L":
        if len(left) !=0:
            right.append(left.pop())
    if command[0] == "D":
        if len(right)!=0:
            left.append(right.pop())

    if command[0]=="B":
        if len(left) != 0:
            left.pop()
    if command[0]=="P":
        left.append(command[1])
left.extend(right)


print(''.join(map(str,left)))


# 질문.
# 처음에 insert써서 했는데 , 시간 초과뜸.
# 그래서 커서기준 좌스택 우스택 나눠서 해봣는데
# 여기서 어떻게 시간을 더 줄ㅇ일 수 있을까요 생선님
    
