import pickle
filepath='example.bin'

def save_data(num,name,height,scores):
    with open(filepath,'wb') as file:
        pickle.dump(num,file)
        pickle.dump(name,file)
        pickle.dump(height,file)
        pickle.dump(scores,file)

def load_data():
    with open(filepath,'rb') as file:
        num=pickle.load(file)
        name=pickle.load(file)
        height=pickle.load(file)
        scores=pickle.load(file)
    return num,name,height,scores

num,name,height=123, '홍길동',180.5
scores={'mid':90, 'fin':95, 'rep':10, 'att':10}
save_data(num,name,height,scores)
r_num,r_name,r_height,r_scores=load_data()

print(r_num)
print(r_name)
print(r_height)
print(r_scores)