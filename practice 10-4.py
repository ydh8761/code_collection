def input_scores():
    s=[]
    i=1
    while True:
        n=int(input(f'#{i}?'))
        if n<0:
            break
        s.append(n)
        i+=1
    return s

def get_average(s):
    total=0
    for n in s:
        total+=n
    return total/len(s)

def show_scores(s):
    for n in s:
        print(n,end=' ')

    print()

def search(lst,n):
    if n not in lst:
        return None
    
    return lst.index(n)

print('[점수 입력]')
scores=input_scores()
print()
print('[점수 출력]')
show_scores(scores)
print()
avg=get_average(scores)
print(f'평균: {avg:.1f}')
print()
print('[검색]')
s=int(input('찾고자 하는 점수는? '))
idx=search(scores,s)
if idx != None:
    print(f'{s}점은 {idx+1}번 학생의 점수입니다.')
else:
    print(f'{s}점을 받은 학생은 없습니다.')