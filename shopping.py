shopping_bag=[]
while True:
    item=input('상품명? ')
    if item=='':
        break
    print('장바구니에',item,'이(가) 담겼습니다.')
    print()
    shopping_bag.append(item)
 
print()
print('>>> 장바구니 보기:', shopping_bag)