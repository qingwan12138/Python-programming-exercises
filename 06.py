import math
C,H=50,30
# D=[]
Q=[]
D=(input("请输入D的取值：").split(","))
print(D)
for item in range(len(D)):
    Q.append(int(math.sqrt((2*C*int(D[item]))/H)))
print(Q)

