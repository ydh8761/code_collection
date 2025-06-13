import os

filename="example.txt"
if os.path.exists(filename):
    file=open(filename,'w')
    file.close()
    print('파일 열고 닫기 완료')
else:
    print(f'ERROR: {filename}이 존재하지 않습니다.')

print('끝')