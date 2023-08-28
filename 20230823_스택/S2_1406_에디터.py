'''처음 시도한 코드(틀린 코드)'''
# word = list(input())
# length = len(word)
# idx = len(word)

# n = int(input())
# for i in range(n):
#     command = input().split()
#     if command[0] == "L":
#         if idx == 0:
#             continue
#         idx -= 1
    
#     if command[0] == "D":
#         if idx == length:
#             continue
#         idx += 1

#     if command[0] == "B":
#         if idx == 0:
#             continue
#         word.remove(word[idx-1])
#         idx -= 1
#         length -= 1

#     if command[0] == "P":
#         word.insert(idx, command[1])
#         idx += 1
#         length += 1

# for i in word:
#     print(i, end="")

'''참고사항'''
# remove가 시간복잡도 O(N)이라 에바인듯 
# idx(커서위치), length(총 단어길이)로 구현하려고 했음
#####################################################

import sys 
input = sys.stdin.readline

# 커서기준 왼쪽, 오른쪽 스택 사용
left = list(input().rstrip())
right = []

n = int(input())
for i in range(n):
    command = input().rstrip().split()
    # L
    if command[0] == "L":
        if len(left) == 0:
            continue
        right.append(left.pop())
    # D
    if command[0] == "D":
        if len(right) == 0:
            continue
        left.append(right.pop())
    # B
    if command[0] == "B":
        if len(left) == 0:
            continue
        left.pop()
    # P
    if command[0] == "P":
        left.append(command[1])

    #print(left, right)


# 왼쪽은 정순, 오른쪽 역순
# 방법 1.
for i in left:
    print(i, end="")

for i in range(len(right)):
    print(right.pop(), end="")    

# 방법 2.
left += reversed(right)
print(''.join(left))

'''참고사항'''
# push, pop O(1)이므로 0.3초안에 괜찮을듯
# join은 split과 반대되는 메소드라고 생각하면 편할듯
