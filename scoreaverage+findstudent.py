print('[점수 입력]')
listscore = []
for i in range(3):
    score = int(input(f'#{i+1}? '))
    listscore.append(score)

print('[점수 출력]')
print('입력 점수:', listscore[0], listscore[1], listscore[2])
print('평균:', sum(listscore)/len(listscore))

print('[검색]')
find=int(input('찾고자 하는 점수는? '))
for i in range(3):
    if listscore[i] == find:
        print(find,'점은',f'{i+1}번 학생의 점수입니다.')
        break