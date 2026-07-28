arr=[]
print("请输入多行文本，即将将每行中的所有字母转换为大写后输出：\n")
while True :
    items=input()
    if items == "#" :
        break
    arr.append(items.upper())
for _ in arr :
    print(_)


