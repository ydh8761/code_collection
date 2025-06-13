def input_num_of_population():
    nPeople=[]
    for f in range(4):
        n=int(input(f'{f+1}층 인원수는? '))
        nPeople.append(n)
    return nPeople

def show_num_of_population(p):
    cnt=len(p)
    for i in range(cnt):
        print(f'{i+1}층 인원수는 {p[i]}명입니다.')

def get_total(lst):
    total=lst[0]+lst[1]
    total+=lst[2]
    total+=lst[3]
    return total
    
population=input_num_of_population()
show_num_of_population(population)
total=get_total(population)
print(f'총 거주인원수는 {total}명입니다.')