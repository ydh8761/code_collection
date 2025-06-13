def buy(sbag):
    print('[구입]')
    item=input('상품명? ')
    if item=='':
        return False
    
    sbag.append(item)
    print(f'장바구니에 {item}이(가) 담겼습니다\n')
    return True

def show(sbag):
    print('\n>>> 장바구니 보기: ', end='')
    print(sbag)

shopping_bag=[]
while True:
    if buy(shopping_bag)==False:
        break

show(shopping_bag)