n = int(input())
cnt = 0 # 그룹 단어 갯수

for i in range(n):
    check = True # 그룹 단어인지 체크할 변수
    word = input()
    for j in range(len(word)-2): # out of range 방지
        
        # 현재 위치 단어와 다음 위치 단어가 다르고, 현재 위치 단어가 2칸뒤의 단어들부터 존재하면 그룹단어 x
        if word[j] != word[j+1] and word[j] in word[j+2:]: 
            check = False
            break

    if check == True:
        cnt += 1
print(cnt)