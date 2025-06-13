import os
filename='shopping_bag.txt'

def show(sbag):
    print('\n>>> 장바구니 보기: ', end='')
    print(sbag)

def buy(sbag):
    print('[구입]')
    item=input('상품명? ')
    if item=='':
        return False
    
    sbag.append(item)
    print(f'장바구니에 {item}이(가) 담겼습니다\n')
    return True

def save_data(sbag,filepath):
    with open(filepath,'w') as file:
        for item in sbag:
            file.write(f'{item}\n')

def load_data(filepath):
    lines=[]
    with open(filepath, 'r') as file:
        for line in file:
            lines.append(line.strip('\n'))

    return lines

if os.path.exists(filename):
    print('[파일 읽기]')
    shopping_bag=load_data(filename)
    show(shopping_bag)

else:
    shopping_bag=[]

while True:
    if buy(shopping_bag)==False:
        break

show(shopping_bag)
save_data(shopping_bag,filename)