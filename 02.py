# for 循环
# num=int(input("请输入你想计算的阶乘："))
# score = 1
# for item in range(1,num+1):
#     score *=item
# print(f"{score}")

# 嵌套
def Factorial(x) :
    if x == 0:
        return 1
    return x*Factorial(x-1)
num=int(input("请输入你想计算的阶乘："))
print(Factorial(num))

