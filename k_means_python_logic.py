import math
from matplotlib import pyplot as plt

data=[[1,1],[1,0],[0,2],[2,4],[3,5]]

a=0
b=2
c1=data[a]
c2=data[b]
d1=[]
d2=[]
k=0

class1=[]
class2=[]
class3=[]
class4=[]

i=1
k=0
while i==1:
    print("c1:",c1,"c2:",c2)
    for i in range(len(data)):
        q=math.sqrt((data[i][0]-c1[0])**2 + (data[i][1]-c1[1])**2)
        w = math.sqrt((data[i][0] - c2[0]) ** 2 + (data[i][1] - c2[1]) ** 2)
        d1.append(q)
        d2.append(w)
    print("d1:", d1)
    print("d2:", d2)
    for j in range(len(data)):
        if d1[j]<d2[j]:
            class1.append(data[j])
        else:
            class2.append(data[j])
    k=k+1
    print("k=",k)
    print("class1:",class1)
    print("class2:",class2)
    print("class3:",class3)
    print("class4:",class4)
    if class1==class3 and class2==class4:
        i=0
        print("clusters=",k-1)
        x=[]
        y=[]
        for p in range(len(class1)):
            x.append(class1[p][0])
            y.append(class1[p][1])
        plt.scatter(x,y,label="class1")
        x = []
        y = []
        for p in range(len(class2)):
            x.append(class2[p][0])
            y.append(class2[p][1])
        plt.scatter(x, y, label="class2")
        plt.grid()
        plt.legend()
        plt.show()
        exit()
    else:
        class3=class1
        class4=class2
    x1=0
    y1=0
    for n in range(len(class1)):
        x1=x1+class1[n][0]
        y1=y1+class1[n][1]
    x2 = 0
    y2 = 0
    for m in range(len(class2)):
        x2 = x2 + class2[m][0]
        y2 = y2 + class2[m][1]
    c1=[x1/(len(class1)),y1/(len(class1))]
    c2=[x2/(len(class2)),y2/(len(class2))]
    d1=[]
    d2=[]
    class1=[]
    class2=[]
    i=1
