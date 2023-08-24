import sys
T = int(sys.stdin.readline())

for _ in range(T):
    
    stack = []
    S = sys.stdin.readline().rstrip()
    # print(S)해보니까 개행이 자동으로 적혀있길래 찾아보니 sys.stdin.readline()은 개행이 자동으로 적힌다고 함 -- rstrip()으로 해결
    
    # VPS를 만족하기 위해서는 (,)의 짝이 맞아야된다고 생각.
    # 그렇다면 일단 (와 )의 갯수가 같아야 됨
    # 일단 VPS이려면 ( 시작이어야 함 -> S를 검사 -> for문
    for i in S:
        if i == '(':
            stack.append(i)
        # 갯수가 같아야 한다고 생각했기때문에 ( 를 넣어주고 )가 나올때 없애버리면 결국 스택은 비어짐 == 길이 0 쓰면 될 듯
        else:
            # stack.pop()  ------ 에러

            # 첫번째로 )가 나오면 스택에 비어있기때문에 pop을 할 수 없네
            # 그럼 일단 비어있으면 vps가 아님 -> 비어있다고 바로 NO라고 출력하니까 바깥 if 문에서 YES로 인식을 해버림
            if len(stack) == 0: # -> 결국 마지막에 길이가 0이면 YES 0이 아니면 NO 이니까 1개를 박아두면 0이 되지 않음
                # print('NO')
                stack.append(i)
                break
            else: # 스택이 비어있지 않을때는 정상 진행
                stack.pop()
           
    if len(stack) == 0:
        print('YES')
    else:
        print('NO') 

#후기 : 처음엔 첫번째 인덱스와 그 뒤 몇번째 인덱스가 짝이 맞는지 비교해야한다고 생각하니 답이 안 나옴 ex)s[i] == ')' and s[i+1] == '('
#       스택을 이용하는 문제라는 걸 알고있었기때문에 append, pop을 이용하는 방법일 거라고 생각
#       스택을 활용하는 문제라는 걸 알고있었기때문이지 그냥 냅다 문제 받았으면 풀기 힘들었을 듯