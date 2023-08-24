import sys
N = int(sys.stdin.readline())

#그냥 input으로 하면 시간 초과
#왜? 
#input()은 sys.stdin.readline()보다 느리다.
#input()은 동적으로 할당되는 메모리를 사용한다.
#sys.stdin.readline()은 정적으로 할당되는 메모리를 사용한다.
#따라서 input()은 시간이 더 걸린다. - 시간초과
stack = []

###########이렇게 하니까 숫자를 입력하지 않는 커맨드가 들어오면 에러가 난다.
# for _ in range(N):
#     command, num = input().split()

#     if command =='push':
#         lis.append(num)
#         print(*lis)
#     elif command == 'pop':
#         if len(lis) == 0 :
#             print(-1)
#         else:
#             pop_lis = lis.pop()
#             print(pop_lis)
#     elif command == 'size':
#         print(len(lis))
#     elif command == 'empty':
#         if len(lis) == 0 :
#             print(1)
#         else:
#             print(0)
#     else :
#         if len(lis) == 0 :
#             print(-1)
#         else:
#             print(lis[len(lis)-1])


for _ in range(N):             
    command = sys.stdin.readline().split()  #처음 생각과 다른 점 - 리스트로 입력되기때문에 인덱스를 사용할 수 있음
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])

## 피드백
좋은 공부였다고 생각합니다. 지금은 상관없지만, 나중에는 거의 대부분 sys.stdin.readline을 사용해야하므로 습관을 들여놓으면 좋습니다.
나도 input받을때, (command, num) 이런 식으로 처음에 받았는데, 찍어가 보면서 바꾸는건 당연한겁니다.
split하면 그 자체로 list로 던져주기때문에 그대로 써도될거같고, 
            
