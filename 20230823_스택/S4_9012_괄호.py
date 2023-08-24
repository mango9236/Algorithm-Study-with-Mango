# 8/24

n = int(input())

# 괄호문제: 완벽한 대칭괄호쌍을 만들기
# VPS: Valid Parenthesis String을 만들기
for i in range(n):
    parenthesis = input()
    stack = []
    for j in parenthesis:
        if j == '(':
            stack.append(j)
        else:
            # ( 없는데 ) 만나면 이미 글러먹음
            if len(stack) == 0:
                stack.append(j)
                break

            # ) 만나면 젤 마지막에 있는거 --> ( 빼기 
            else:
                stack.pop()
    
    # 전부 다 쌍으로 없어졌으면 VPS
    if len(stack) == 0:
        print('YES')
        
    else:
        print('NO')

'''참고사항'''
# 스택의 push, pop 개념을 숙지하면 쉬웠음. () 두개가 만나면 사라진다라고 이해했으면 쉽게 풀 수있을듯?

# Q. 예상질문: ( 남으면요? 
# A. 그래서 len(stack) == 0 이면 YES라고 줬음.
