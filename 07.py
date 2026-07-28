# map(函数, 可迭代对象)
x,y=map(int,input().split(","))
lst=[[i*j for j in range(y)] for i in range(x)]
print(lst)


