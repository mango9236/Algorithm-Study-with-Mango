N = int(input())
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
    command = input().split()  #리스트로 입력되기때문에 인덱스를 사용할 수 있음
    if command[0] == 'push':
        stack.append(command[1])
        print(*stack)
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
            