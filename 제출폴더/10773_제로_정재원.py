import sys
K = int(sys.stdin.readline())
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