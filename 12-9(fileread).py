lines=[]
with open('example.txt','r',encoding='utf-8') as file:
    while True:
        line=file.readline()

        if line=='':
            break
        lines.append(line.strip())

print(lines)