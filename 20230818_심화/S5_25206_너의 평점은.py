# 미리 학점 딕셔너리로 저장
score = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0, "P": 0.0}

all_sum = 0 # 모든 학점 합
all_hackjum = 0 # 모든 총 이수 학점 

for i in range(20):
    lst = list(map(str, input().split())) # 과목, 이수학점, 학점
    if (lst[2] == "P"): # 학점 pass면 걍 넘어감
        continue
    hackjum = float(lst[1]) # 이수학점
    s = score[lst[2]] # 학점

    # 평균 = 총 학점 합 / 총 이수학점
    all_hackjum += hackjum
    all_sum += hackjum * s

print(all_sum/all_hackjum)    