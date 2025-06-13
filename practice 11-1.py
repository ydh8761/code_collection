class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def show(self):
        print(f'({self.x},{self.y})')
        
    def set(self,x,y):
        self.x=x
        self.y=y

    def get(self):
        return self.x,self.y
    
def test():
    p1=Point()
    p2=Point(2,3)

    p1.show()

    p1.set(10,20);p1.show()

    p2.show()

    x,y=p2.get()
    print(f'x={x},y={y}')

if __name__=='__main__':
    test()