croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

# 크로아티아 알파벳이 word안에 있으면 바꿔줌
for i in croatia :
    word = word.replace(i, '*') # ex) c= -> * : * 한개가 단어하나를 의미하므로 

# 그냥 길이 세어 주면 됨.
print(len(word))
