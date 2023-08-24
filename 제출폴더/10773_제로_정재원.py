import sys
K = int(sys.stdin.readline()) #피드백 반영 : sys 쓰는 습관들이기
stack = []

for _ in range(K) :
    N = int(sys.stdin.readline())
    if N != 0 :
        stack.append(N)
        # print(stack)
    else :
        stack.pop()
        # print(stack)
        
print(sum(stack))

#후기 : 그냥 스택 문제 그 자체로 난이도가 어렵진 않았다.
