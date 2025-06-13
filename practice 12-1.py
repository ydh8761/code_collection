def show_file(filename):
    with open(filename, mode='r',encoding='cp949') as file:
        i=1
        while True:
            line=file.readline()

            if line=='':
                break
            print(f'{i}: {line.strip()}')
            i+=1

fn=input('파일명? ')
show_file(fn)