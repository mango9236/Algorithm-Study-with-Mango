# 8/24

# 괄호문제: 완벽한 대칭괄호쌍을 만들기
line = input()

# 그냥 .이 아니면 반복
while line[0] != ".":
    stack = []
    # 한글자씩 체크 
    for letter in line:
        # ( or [ 이면 append
        if letter == '(' or letter == '[':
            stack.append(letter)

        # ] 
        elif letter == "]":
            # 없는데 ] 넣으면 나가리지 ㅋㅋ
            if len(stack) == 0:
                stack.append(letter)
                break
            # 마지막게 [ 면 [] 만들수있음. -> pop해주기
            elif stack[-1] == "[":
                stack.pop()
            # (] --> 나가리 
            else:
                stack.append(letter)
                break

        # )
        elif letter == ")":
            # 없는데 ) 넣으면 나가리지 ㅋㅋ
            if len(stack) == 0:
                stack.append(letter)
                break
            # 마지막게 ( 면 () 만들수있음. -> pop해주기
            elif stack[-1] == "(":
                stack.pop()
            # [) --> 나가리 
            else:
                stack.append(letter)
                break

    # 모두 다 짝이 맞추어 지면 OK
    if len(stack) == 0:
        print("yes")
    
    else:
        print("no")

    # 새로운 라인 받아주기
    line = input()

'''참고사항'''
# 괄호 문제랑 별반 다를게 없는데 예외처리 case 해주는게 조금 복잡했을거라 생각함
# 근데 () [] 두개로 바뀐거지 각각 생각해서 복붙이니까 한 케이스만 생각하면 됬을거라 생각함

# TIP. 지금처럼 while문 돌리는데 조건 있을때
# n = input
# while ~~~:
#   n = input 이런식으로 받으면 조건문 체크하고 돌릴수있음 --> 처음부터 "."이 올 수 있잖아?
