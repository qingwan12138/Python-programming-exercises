# 分行版
# for item in range(2000,3201):
#     if item % 7==0 and item %5 !=0 :
#         print(f"{item},")
# 一行版
# for item in range(2000,3201):
#     if item % 7==0 and item %5 !=0 :
#         print(f"{item},",end="")

# 列表版
res=[]
for item in range(2000,3201):
    if item % 7==0 and item %5 !=0 :
        res.append(str(item))
print(",".join(res))
# "分隔符".join(可迭代对象)
# 作用：把列表 / 元组里全部字符串，用你写的分隔符拼接成一整行字符串
# 关键点：join 只能拼接字符串，数字要先转 str()