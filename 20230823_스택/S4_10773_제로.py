# 8/24

import sys
input = sys.stdin.readline

k = int(input())
lst = []
for i in range(k):
    n = int(input())
    if n == 0:
        #lst = lst[:-1] 
        lst.pop()
    else:
        lst.append(n) 
print(sum(lst))


'''참고사항'''
# 시간복잡도 측면에서 슬라이싱보다 pop이 더 빠르다.
# 시간복잡도 [a:b]는 O(b-a)이고, pop은 O(1)이다.
# 나도 비교해봤는데 슬라이싱은 약 5000ms = 5초, pop은 약 70ms 걸렸다.
