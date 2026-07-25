# 100+ 道 Python 3 挑战性编程练习

> 翻译说明：本文仅翻译题目、提示、示例与说明文字。为避免改变程序语法、变量名或输出行为，所有代码块均按英文原文保留。原文中部分代码使用 Python 2 语法，或存在题意与参考答案不完全一致、代码围栏缺失等情况，本译文不对这些内容作技术修正。

## 1. 难度说明

### 难度 1：初级

初级指刚刚完成 Python 入门课程的学习者。他通常能够使用 1～2 个 Python 类或函数解决一些问题，答案一般可以直接从教材中找到。

### 难度 2：中级

中级指刚学完 Python，但此前已经具备较强编程基础的学习者。他应当能够解决需要组合使用多个 Python 类或函数的问题，答案通常无法直接从教材中找到。

### 难度 3：高级

高级学习者应使用 Python、更丰富的库函数、数据结构和算法解决较复杂的问题，并能够综合运用多个 Python 标准库和高级技巧。

----

## 2. 题目模板

题目

提示

参考答案

----

## 3. 题目

### 题目 1

难度 1

题目：
编写一个程序，找出 2000 到 3200 之间（包含 2000 和 3200）所有能被 7 整除、但不是 5 的倍数的数。
将得到的数字在一行中以逗号分隔的形式输出。

提示：
考虑使用 `range(起始值, 结束值)` 方法。


参考答案：

```python
l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print(','.join(l))
```


### 题目 2

难度 1

题目：
编写一个程序，计算给定数字的阶乘。
假设向程序输入：
8
则输出应为：
40320

提示：
题目中给出的输入数据均视为通过控制台输入。


参考答案：

```python
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x=int(input())
print(fact(x))
```


### 题目 3

难度 1

题目：
给定一个整数 n，编写程序生成一个字典。字典中包含 `(i, i*i)` 形式的键值对，其中 i 为 1 到 n 之间的整数（包含 1 和 n），然后输出该字典。
假设向程序输入：
8
则输出应为：
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

提示：
题目中给出的输入数据均视为通过控制台输入。
考虑使用 `dict()`。


参考答案：

```python
n=int(input())
d=dict()
for i in range(1,n+1):
    d[i]=i*i

print(d)
```


### 题目 4

难度 1

题目：
编写一个程序，从控制台接收一串以逗号分隔的数字，并生成包含这些数字的列表和元组。
假设向程序输入：
34,67,55,33,12,98
则输出应为：
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

提示：
题目中给出的输入数据均视为通过控制台输入。
`tuple()` 方法可以将列表转换为元组。


参考答案：

```python
values=input()
l=values.split(",")
t=tuple(l)
print(l)
print(t)
```


### 题目 5

难度 1

题目：
定义一个至少包含以下两个方法的类：
- `getString`：从控制台读取一个字符串。
- `printString`：以大写形式输出该字符串。

另外，请包含一个简单的测试代码，用于测试这些类方法。

提示：
使用 `__init__` 方法初始化相关参数。


参考答案：

```python
class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()
    
    def printString(self):
        print(self.s.upper())

strObj = InputOutString()
strObj.getString()
strObj.printString()
```


### 题目 6

难度 2

题目：
编写一个程序，根据下列公式计算并输出 Q 的值：

Q = √[(2 × C × D) / H]

C 和 H 为固定值：
C = 50，H = 30。
D 为变量，其值应以逗号分隔的形式输入程序。

示例：
假设输入序列为：
100,150,180
程序输出应为：
18,22,24

提示：
若计算结果为小数，应将其四舍五入为最接近的整数。例如，若结果为 26.0，则输出 26。
题目中给出的输入数据均视为通过控制台输入。


参考答案：

```python
import math
c=50
h=30
value = []
items=[x for x in input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print(','.join(value))
```


### 题目 7

难度 2

题目：
输入两个数字 X、Y，生成一个二维数组。数组第 i 行、第 j 列的元素值应为 `i*j`。

注意：i = 0, 1, ..., X-1；j = 0, 1, ..., Y-1。

示例：
假设输入为：
3,5
则输出应为：
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

提示：
题目中给出的输入数据均视为通过控制台以逗号分隔的形式输入。


参考答案：

```python
input_str = input()
dimensions=[int(x) for x in input_str.split(',')]
rowNum=dimensions[0]
colNum=dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col

print(multilist)
```


### 题目 8

难度 2

题目：
编写一个程序，接收一串以逗号分隔的单词，将这些单词按字母顺序排序后，再以逗号分隔的形式输出。

假设输入为：
without,hello,bag,world
则输出应为：
bag,hello,without,world

提示：
题目中给出的输入数据均视为通过控制台输入。


参考答案：

```python
items=[x for x in input().split(',')]
items.sort()
print(','.join(items))
```


### 题目 9

难度 2

题目：
编写一个程序，接收多行文本作为输入，并将每行中的所有字母转换为大写后输出。

假设输入为：
Hello world
Practice makes perfect
则输出应为：
HELLO WORLD
PRACTICE MAKES PERFECT

提示：
题目中给出的输入数据均视为通过控制台输入。


参考答案：

```python
lines = []
while True:
    s = input()
    if s:
        lines.append(s.upper())
    else:
        break;

for sentence in lines:
    print(sentence)
```


### 题目 10

难度 2

题目：
编写一个程序，接收一串以空格分隔的单词，删除所有重复单词并按字母数字顺序排序后输出。

假设输入为：
hello world and practice makes perfect and hello world again
则输出应为：
again and hello makes perfect practice world

提示：
题目中给出的输入数据均视为通过控制台输入。
可以使用 `set` 自动删除重复数据，再使用 `sorted()` 对数据排序。


参考答案：

```python
s = input()
words = [word for word in s.split(" ")]
print(" ".join(sorted(list(set(words)))))
```


### 题目 11

难度 2

题目：
编写一个程序，接收一串以逗号分隔的 4 位二进制数，检查它们是否能被 5 整除，并将能够被 5 整除的数以逗号分隔的形式输出。

示例：
输入：
0100,0011,1010,1001
输出：
1010

注意：假设数据通过控制台输入。

提示：
题目中给出的输入数据均视为通过控制台输入。


参考答案：

```python
value = []
items=[x for x in input().split(',')]
for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)

print(','.join(value))
```


### 题目 12

难度 2

题目：
编写一个程序，找出 1000 到 3000 之间（包含两端）所有各位数字均为偶数的数。
将得到的数字在一行中以逗号分隔的形式输出。

提示：
题目中给出的输入数据均视为通过控制台输入。


参考答案：

```python
values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print(",".join(values))
```


### 题目 13

难度 2

题目：
编写一个程序，接收一个句子并统计其中字母和数字的数量。

假设输入为：
hello world! 123
则输出应为：
LETTERS 10
DIGITS 3

提示：
题目中给出的输入数据均视为通过控制台输入。


参考答案：

```python
s = input()
d={"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print("LETTERS", d["LETTERS"])
print("DIGITS", d["DIGITS"])
```


### 题目 14

难度 2

题目：
编写一个程序，接收一个句子并统计其中大写字母和小写字母的数量。

假设输入为：
Hello world!
则输出应为：
UPPER CASE 1
LOWER CASE 9

提示：
题目中给出的输入数据均视为通过控制台输入。


参考答案：

```python
s = input()
d={"UPPER CASE":0, "LOWER CASE":0}
for c in s:
    if c.isupper():
        d["UPPER CASE"]+=1
    elif c.islower():
        d["LOWER CASE"]+=1
    else:
        pass
print("UPPER CASE", d["UPPER CASE"])
print("LOWER CASE", d["LOWER CASE"])
```


### 题目 15

难度 2

题目：
给定一个数字作为 a 的值，编写程序计算 `a + aa + aaa + aaaa`。

假设输入为：
9
则输出应为：
11106

提示：
题目中给出的输入数据均视为通过控制台输入。


参考答案：

```python
a = input()
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
n4 = int( "%s%s%s%s" % (a,a,a,a) )
print(n1+n2+n3+n4)
```


### 题目 16

难度 2

题目：
使用列表推导式筛选列表中的所有奇数。列表通过一串以逗号分隔的数字输入。

假设输入为：
1,2,3,4,5,6,7,8,9
则输出应为：
1,3,5,7,9

提示：
题目中给出的输入数据均视为通过控制台输入。


参考答案：

```python
values = input()
numbers = [x for x in values.split(",") if int(x)%2!=0]
print(",".join(numbers))
```


### 题目 17

难度 2

题目：
根据控制台输入的交易记录，计算银行账户的净余额。交易记录格式如下：
D 100
W 200

其中，D 表示存款，W 表示取款。

假设输入为：
D 300
D 300
W 200
D 100
则输出应为：
500

提示：
题目中给出的输入数据均视为通过控制台输入。


参考答案：

```python
netAmount = 0
while True:
    s = input()
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation=="D":
        netAmount+=amount
    elif operation=="W":
        netAmount-=amount
    else:
        pass
print(netAmount)
```


### 题目 18

难度 3

题目：
某网站要求用户输入用户名和密码进行注册。请编写一个程序，检查用户输入的密码是否合法。

密码检查标准如下：
1. 至少包含一个 `[a-z]` 范围内的小写字母；
2. 至少包含一个 `[0-9]` 范围内的数字；
3. 至少包含一个 `[A-Z]` 范围内的大写字母；
4. 至少包含一个 `[$#@]` 中的字符；
5. 密码最短长度为 6；
6. 密码最长长度为 12。

程序应接收一串以逗号分隔的密码，并按照上述标准进行检查。符合条件的密码应以逗号分隔的形式输出。

示例：
若输入密码为：
ABd1234@1,a F1#,2w3E*,2We3345
则输出应为：
ABd1234@1

提示：
题目中给出的输入数据均视为通过控制台输入。


参考答案：

```python
import re
value = []
items=[x for x in input().split(',')]
for p in items:
    if len(p)<6 or len(p)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    elif re.search("\s",p):
        continue
    else:
        pass
    value.append(p)
print(",".join(value))
```


### 题目 19

难度 3

题目：
编写一个程序，将 `(姓名, 年龄, 身高)` 元组按升序排序，其中姓名为字符串，年龄和身高为数字。元组通过控制台输入。

排序规则如下：
1. 先按姓名排序；
2. 姓名相同时，再按年龄排序；
3. 姓名和年龄都相同时，再按第三个字段排序。

优先级为：姓名 > 年龄 > 第三个字段。

假设输入为：
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
则输出应为：
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

提示：
题目中给出的输入数据均视为通过控制台输入。
可以使用 `itemgetter` 设置多个排序键。


参考答案：

from operator import itemgetter, attrgetter

```python
l = []
while True:
    s = input()
    if not s:
        break
    l.append(tuple(s.split(",")))

print(sorted(l, key=itemgetter(0,1,2)))
```


### 题目 20

难度 3

题目：
定义一个生成器，用于遍历给定范围 0 到 n 之间所有能被 7 整除的数。

提示：
考虑使用 `yield`。


参考答案：

```python
def putNumbers(n):
    i = 0
    while i<n:
        j=i
        i=i+1
        if j%7==0:
            yield j

for i in reverse(100):
    print(i)
```


### 题目 21

难度 3

题目：
一个机器人从平面上的原点 `(0,0)` 出发，可以按照给定步数向上、下、左、右移动。机器人的移动轨迹格式如下：
UP 5
DOWN 3
LEFT 3
RIGHT 2
...

方向后的数字表示移动步数。请编写程序，在执行一系列移动后，计算机器人当前位置到原点的距离。若距离为小数，则输出最接近的整数。

示例：
若输入为：
UP 5
DOWN 3
LEFT 3
RIGHT 2
则输出应为：
2

提示：
题目中给出的输入数据均视为通过控制台输入。


参考答案：

```python
import math
pos = [0,0]
while True:
    s = input()
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction=="UP":
        pos[0]+=steps
    elif direction=="DOWN":
        pos[0]-=steps
    elif direction=="LEFT":
        pos[1]-=steps
    elif direction=="RIGHT":
        pos[1]+=steps
    else:
        pass

print(int(round(math.sqrt(pos[1]**2+pos[0]**2))))
```


### 题目 22

难度 3

题目：
编写一个程序，统计输入文本中各单词出现的频率。输出时应先按单词的字母数字顺序排序。

假设输入为：
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
则输出应为：
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1

提示：
题目中给出的输入数据均视为通过控制台输入。


参考答案：

```python
freq = {}   # frequency of words in text
line = input()
for word in line.split():
    freq[word] = freq.get(word,0)+1

words = freq.keys()
words.sort()

for w in words:
    print("%s:%d" % (w,freq[w]))
```


### 题目 23

难度 1

题目：
编写一个方法，计算给定数字的平方。

提示：
使用 `**` 运算符。


参考答案：

```python
def square(num):
    return num ** 2

print(square(2))
print(square(3))
```


### 题目 24

难度 1

题目：
Python 提供了许多内置函数。当你不知道如何使用某个函数时，可以查阅在线文档或相关书籍。除此之外，Python 的每个内置函数本身也带有内置文档。

请编写一个程序，输出若干 Python 内置函数的文档，例如 `abs()`、`int()`、`raw_input()`。

同时，也请为你自己定义的函数添加文档。

提示：
内置文档属性为 `__doc__`。


参考答案：

```python
print(abs.__doc__)
print(int.__doc__)
print(input.__doc__)

def square(num):
    '''Return the square value of the input number.
    
    The input number must be integer.
    '''
    return num ** 2

print(square(2))
print(square.__doc__)
```


### 题目 25

难度 1

题目：
定义一个类，使其同时具有一个类属性和一个同名的实例属性。

提示：
实例属性需要在 `__init__` 方法中定义。
可以通过构造参数初始化对象，也可以稍后再设置属性值。


参考答案：

```python
class Person:
    # Define the class parameter "name"
    name = "Person"
    
    def __init__(self, name = None):
        # self.name is the instance parameter
        self.name = name

jeffrey = Person("Jeffrey")
print("%s name is %s" % (Person.name, jeffrey.name))

nico = Person()
nico.name = "Nico"
print("%s name is %s" % (Person.name, nico.name))
```


### 题目 26

题目：
定义一个函数，计算两个数的和。

提示：
定义一个接收两个数字参数的函数，在函数中计算它们的和并返回结果。


参考答案：

```python
def SumFunction(number1, number2):
	return number1+number2

print(SumFunction(1,2))
```


### 题目 27

题目：
定义一个函数，将整数转换为字符串并在控制台中输出。

提示：
使用 `str()` 将数字转换为字符串。


参考答案：

```python
def printValue(n):
    print(str(n))

printValue(3)
```


### 题目 28

题目：
定义一个函数，将整数转换为字符串并在控制台中输出。

提示：
使用 `str()` 将数字转换为字符串。


参考答案：

```python
def printValue(n):
    print(str(n))

printValue(3)
```


### 题目 29

题目：
定义一个函数，接收两个字符串形式的整数，计算它们的和并在控制台中输出。

提示：
使用 `int()` 将字符串转换为整数。


参考答案：

```python
def printValue(s1,s2):
    print(int(s1)+int(s2))

printValue("3","4")
```


### 题目 30

题目：
定义一个函数，接收两个字符串作为输入，将它们拼接后在控制台中输出。

提示：
使用 `+` 拼接字符串。


参考答案：

```python
def printValue(s1,s2):
    print(s1+s2)

printValue("3","4") #34
```


### 题目 31

题目：
定义一个函数，接收两个字符串作为输入，并在控制台中输出长度较大的字符串。若两个字符串长度相同，则逐行输出这两个字符串。

提示：
使用 `len()` 函数获取字符串长度。


参考答案：

```python
def printValue(s1,s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1>len2:
        print(s1)
    elif len2>len1:
        print(s2)
    else:
        print(s1)
        print(s2)
        
printValue("one","three")

```


### 题目 32

题目：
定义一个函数，接收一个整数作为输入。如果该数为偶数，则输出 `It is an even number`；否则输出 `It is an odd number`。

提示：
使用 `%` 运算符判断一个数是奇数还是偶数。


参考答案：

```python
def checkValue(n):
    if n%2 == 0:
        print("It is an even number")
    else:
        print("It is an odd number")
        
checkValue(7)


### 题目 33

题目：
定义一个函数，输出一个字典。字典的键为 1 到 3 之间的数字（包含 1 和 3），值为对应键的平方。

提示：
使用 `dict[key] = value` 的形式向字典中添加键值对。
使用 `**` 运算符计算幂。


参考答案：

​```python
def printDict():
    d=dict()
    d[1]=1
    d[2]=2**2
    d[3]=3**2
    print(d)
        
printDict()
```


### 题目 34

题目：
定义一个函数，输出一个字典。字典的键为 1 到 20 之间的数字（包含 1 和 20），值为对应键的平方。

提示：
使用 `dict[key] = value` 的形式向字典中添加键值对。
使用 `**` 运算符计算幂。
使用 `range()` 进行循环。


参考答案：

```python
def printDict():
	d=dict()
	for i in range(1,21):
		d[i]=i**2
	print(d)

printDict()
```


### 题目 35

题目：
定义一个函数，生成一个字典。字典的键为 1 到 20 之间的数字（包含 1 和 20），值为对应键的平方。函数只需输出字典中的值。

提示：
使用 `dict[key] = value` 的形式向字典中添加键值对。
使用 `**` 运算符计算幂。
使用 `range()` 进行循环。
可使用 `keys()` 遍历字典的键，也可以使用 `items()` 获取键值对。


参考答案：

```python
def printDict():
	d=dict()
	for i in range(1,21):
		d[i]=i**2
	for (k,v) in d.items():	
		print(v)

printDict()
```


### 题目 36

题目：
定义一个函数，生成一个字典。字典的键为 1 到 20 之间的数字（包含 1 和 20），值为对应键的平方。函数只需输出字典中的键。

提示：
使用 `dict[key] = value` 的形式向字典中添加键值对。
使用 `**` 运算符计算幂。
使用 `range()` 进行循环。
可使用 `keys()` 遍历字典的键，也可以使用 `items()` 获取键值对。


参考答案：

```python
def printDict():
	d=dict()
	for i in range(1,21):
		d[i]=i**2
	for k in d.keys():	
		print(k)

printDict()
```


### 题目 37

题目：
定义一个函数，生成并输出一个列表，其中的值为 1 到 20 之间各数字的平方（包含 1 和 20）。

提示：
使用 `**` 运算符计算幂。
使用 `range()` 进行循环。
使用 `list.append()` 向列表中添加值。


参考答案：

```python
def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print(li)

printList()
```


### 题目 38

题目：
定义一个函数，生成一个列表，其中的值为 1 到 20 之间各数字的平方（包含 1 和 20），然后输出列表中的前 5 个元素。

提示：
使用 `**` 运算符计算幂。
使用 `range()` 进行循环。
使用 `list.append()` 向列表中添加值。
使用 `[n1:n2]` 对列表进行切片。


参考答案：

```python
def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print(li[:5])

printList()
```


### 题目 39

题目：
定义一个函数，生成一个列表，其中的值为 1 到 20 之间各数字的平方（包含 1 和 20），然后输出列表中的最后 5 个元素。

提示：
使用 `**` 运算符计算幂。
使用 `range()` 进行循环。
使用 `list.append()` 向列表中添加值。
使用 `[n1:n2]` 对列表进行切片。


参考答案：

```python
def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print(li[-5:])

printList()
```


### 题目 40

题目：
定义一个函数，生成一个列表，其中的值为 1 到 20 之间各数字的平方（包含 1 和 20），然后输出除前 5 个元素之外的所有值。

提示：
使用 `**` 运算符计算幂。
使用 `range()` 进行循环。
使用 `list.append()` 向列表中添加值。
使用 `[n1:n2]` 对列表进行切片。


参考答案：

```python
def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print li[5:]

printList()
```


### 题目 41

题目：
定义一个函数，生成并输出一个元组，其中的值为 1 到 20 之间各数字的平方（包含 1 和 20）。

提示：
使用 `**` 运算符计算幂。
使用 `range()` 进行循环。
使用 `list.append()` 向列表中添加值。
使用 `tuple()` 将列表转换为元组。


参考答案：

```python
def printTuple():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print(tuple(li))
		
printTuple()
```


### 题目 42

题目：
给定元组 `(1,2,3,4,5,6,7,8,9,10)`，编写程序在一行中输出前半部分的值，在另一行中输出后半部分的值。

提示：
使用 `[n1:n2]` 形式对元组进行切片。


参考答案：

```python
tp=(1,2,3,4,5,6,7,8,9,10)
tp1=tp[:5]
tp2=tp[5:]
print(tp1)
print(tp2)
```


### 题目 43

题目：
给定元组 `(1,2,3,4,5,6,7,8,9,10)`，生成并输出另一个只包含其中偶数元素的元组。

提示：
使用 `for` 遍历元组。
使用 `tuple()` 将列表转换为元组。


参考答案：

```python
tp=(1,2,3,4,5,6,7,8,9,10)
li=list()
for i in tp:
	if tp[i]%2==0:
		li.append(tp[i])

tp2=tuple(li)
print(tp2)
```


### 题目 44

题目：
编写一个程序，接收一个字符串作为输入。如果字符串为 `yes`、`YES` 或 `Yes`，则输出 `Yes`；否则输出 `No`。

提示：
使用 `if` 语句判断条件。


参考答案：

```python
s= raw_input()
if s=="yes" or s=="YES" or s=="Yes":
    print "Yes"
else:
    print "No"
```


### 题目 45

题目：
使用 `filter` 函数，从列表 `[1,2,3,4,5,6,7,8,9,10]` 中筛选出偶数。

提示：
使用 `filter()` 过滤列表中的元素。
使用 `lambda` 定义匿名函数。


参考答案：

```python
li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = filter(lambda x: x%2==0, li)
print(evenNumbers)
```


### 题目 46

题目：
使用 `map()` 生成一个列表，其中的元素为列表 `[1,2,3,4,5,6,7,8,9,10]` 中各元素的平方。

提示：
使用 `map()` 生成列表。
使用 `lambda` 定义匿名函数。


参考答案：

```python
li = [1,2,3,4,5,6,7,8,9,10]
squaredNumbers = map(lambda x: x**2, li)
print(squaredNumbers)
```


### 题目 47

题目：
结合使用 `map()` 和 `filter()`，生成一个列表，其中的元素为 `[1,2,3,4,5,6,7,8,9,10]` 中各偶数的平方。

提示：
使用 `map()` 生成列表。
使用 `filter()` 过滤列表元素。
使用 `lambda` 定义匿名函数。


参考答案：

```python
li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = map(lambda x: x**2, filter(lambda x: x%2==0, li))
print(evenNumbers)
```


### 题目 48

题目：
使用 `filter()` 生成一个列表，其中包含 1 到 20 之间的所有偶数（包含 1 和 20）。

提示：
使用 `filter()` 过滤列表元素。
使用 `lambda` 定义匿名函数。


参考答案：

```python
evenNumbers = filter(lambda x: x%2==0, range(1,21))
print(evenNumbers)
```


### 题目 49

题目：
使用 `map()` 生成一个列表，其中包含 1 到 20 之间各数字的平方（包含 1 和 20）。

提示：
使用 `map()` 生成列表。
使用 `lambda` 定义匿名函数。


参考答案：

```python
squaredNumbers = map(lambda x: x**2, range(1,21))
print(squaredNumbers)
```


### 题目 50

题目：
定义一个名为 `American` 的类，其中包含一个名为 `printNationality` 的静态方法。

提示：
使用 `@staticmethod` 装饰器定义类的静态方法。


参考答案：

```python
class American(object):
    @staticmethod
    def printNationality():
        print("America")

anAmerican = American()
anAmerican.printNationality()
American.printNationality()
```


### 题目 51

题目：
定义一个名为 `American` 的类，以及它的子类 `NewYorker`。

提示：
使用 `class 子类(父类)` 的形式定义子类。


参考答案：

```python
class American(object):
    pass

class NewYorker(American):
    pass

anAmerican = American()
aNewYorker = NewYorker()
print(anAmerican)
print(aNewYorker)
```


### 题目 52

题目：
定义一个名为 `Circle` 的类，可以通过半径创建对象。该类包含一个用于计算圆面积的方法。

提示：
使用 `def 方法名(self)` 定义实例方法。


参考答案：

```python
class Circle(object):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14

aCircle = Circle(2)
print aCircle.area()
```


### 题目 53

题目：
定义一个名为 `Rectangle` 的类，可以通过长度和宽度创建对象。该类包含一个用于计算矩形面积的方法。

提示：
使用 `def 方法名(self)` 定义实例方法。


参考答案：

```python
class Rectangle(object):
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def area(self):
        return self.length*self.width

aRectangle = Rectangle(2,10)
print(aRectangle.area())
```


### 题目 54

题目：
定义一个名为 `Shape` 的类及其子类 `Square`。`Square` 类的初始化函数接收边长作为参数。两个类都包含 `area` 方法，其中 `Shape` 的面积默认返回 0，`Square` 的面积返回正方形面积。

提示：
若要重写父类的方法，可以在子类中定义同名方法。


参考答案：

```python
class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l

    def area(self):
        return self.length*self.length

aSquare= Square(3)
print(aSquare.area())
```


### 题目 55

题目：
主动抛出一个 `RuntimeError` 异常。

提示：
使用 `raise` 抛出异常。


参考答案：

```python
raise RuntimeError('something wrong')
```


### 题目 56

题目：
编写一个函数计算 `5/0`，并使用 `try/except` 捕获异常。

提示：
使用 `try/except` 捕获异常。


参考答案：

```python
def throws():
    return 5/0

try:
    throws()
except ZeroDivisionError:
    print("division by zero!")
except Exception, err:
    print('Caught an exception')
finally:
    print('In finally block for cleanup')
```


### 题目 57

题目：
定义一个自定义异常类，并将字符串消息作为其属性。

提示：
定义自定义异常时，需要创建一个继承自 `Exception` 的类。


参考答案：

```python
class MyError(Exception):
    """My own exception class

    Attributes:
        msg  -- explanation of the error
    """
    
    def __init__(self, msg):
        self.msg = msg

error = MyError("something wrong")
```


### 题目 58

题目：
假设电子邮箱地址格式为 `username@companyname.com`，请编写程序输出给定邮箱地址中的用户名。用户名和公司名均只由字母组成。

示例：
若输入邮箱地址为：

john@google.com

则输出应为：

john

题目中给出的输入数据均视为通过控制台输入。

提示：
使用 `\w` 匹配字母或单词字符。


参考答案：

```python
import re
emailAddress = raw_input()
pat2 = "(\w+)@((\w+\.)+(com))"
r2 = re.match(pat2,emailAddress)
print(r2.group(1))
```


### 题目 59

题目：
假设电子邮箱地址格式为 `username@companyname.com`，请编写程序输出给定邮箱地址中的公司名。用户名和公司名均只由字母组成。

示例：
若输入邮箱地址为：

john@google.com

则输出应为：

google

题目中给出的输入数据均视为通过控制台输入。

提示：
使用 `\w` 匹配字母或单词字符。


参考答案：

```python
import re
emailAddress = raw_input()
pat2 = "(\w+)@(\w+)\.(com)"
r2 = re.match(pat2,emailAddress)
print(r2.group(2))
```


### 题目 60

题目：
编写一个程序，接收一串以空白字符分隔的单词，并输出其中完全由数字组成的内容。

示例：
若输入为：

2 cats and 3 dogs.

则输出应为：

['2', '3']

题目中给出的输入数据均视为通过控制台输入。

提示：
使用 `re.findall()` 通过正则表达式查找所有匹配的子字符串。


参考答案：

```python
import re
s = raw_input()
print(re.findall("\d+",s))
```


### 题目 61

题目：
输出 Unicode 字符串 `hello world`。

提示：
使用 `u'字符串'` 的形式定义 Unicode 字符串。


参考答案：

```python
unicodeString = u"hello world!"
print(unicodeString)
```


### 题目 62

题目：
编写一个程序，读取一个 ASCII 字符串，并将其转换为采用 UTF-8 编码的 Unicode 字符串。

提示：
使用 `unicode()` 函数进行转换。


参考答案：

```python
s = input()
u = unicode( s ,"utf-8")
print(u)
```


### 题目 63

题目：
编写一条特殊注释，用于声明 Python 源代码文件采用 Unicode 编码。

提示：
在源代码文件开头添加编码声明。


参考答案：

```python

# -*- coding: utf-8 -*-

#----------------------------------------#
```


### 题目 64

题目：
给定一个通过控制台输入的 n（n > 0），编写程序计算：

`1/2 + 2/3 + 3/4 + ... + n/(n+1)`

示例：
若输入 n 为：

5

则输出应为：

3.55

题目中给出的输入数据均视为通过控制台输入。

提示：
使用 `float()` 将整数转换为浮点数。


参考答案：

```python
n=int(input())
sum=0.0
for i in range(1,n+1):
    sum += float(float(i)/(i+1))
print(sum)
```


### 题目 65

题目：
给定一个通过控制台输入的 n（n > 0），根据下列递推关系计算函数值：

- 当 n > 0 时，`f(n) = f(n-1) + 100`
- `f(0) = 1`

示例：
若输入 n 为：

5

则输出应为：

500

题目中给出的输入数据均视为通过控制台输入。

提示：
可以在 Python 中定义递归函数。


参考答案：

```python
def f(n):
    if n==0:
        return 0
    else:
        return f(n-1)+100

n=int(input())
print(f(n))
```


### 题目 66

题目：
斐波那契数列按下列公式计算：

- 当 n = 0 时，`f(n) = 0`
- 当 n = 1 时，`f(n) = 1`
- 当 n > 1 时，`f(n) = f(n-1) + f(n-2)`

请编写程序，根据控制台输入的 n 计算 `f(n)` 的值。

示例：
若输入 n 为：

7

则输出应为：

13

题目中给出的输入数据均视为通过控制台输入。

提示：
可以在 Python 中定义递归函数。


参考答案：

```python
def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)

n=int(input())
print(f(n))
```


### 题目 67

题目：
斐波那契数列按下列公式计算：

- 当 n = 0 时，`f(n) = 0`
- 当 n = 1 时，`f(n) = 1`
- 当 n > 1 时，`f(n) = f(n-1) + f(n-2)`

请使用列表推导式编写程序，根据控制台输入的 n，以逗号分隔的形式输出从 `f(0)` 到 `f(n)` 的斐波那契数列。

示例：
若输入 n 为：

7

则输出应为：

0,1,1,2,3,5,8,13

提示：
可以在 Python 中定义递归函数。
使用列表推导式基于已有序列生成列表。
使用 `string.join()` 或字符串的 `join()` 方法连接字符串列表。
题目中给出的输入数据均视为通过控制台输入。


参考答案：

```python
def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)

n=int(input())
values = [str(f(x)) for x in range(0, n+1)]
print(",".join(values))
```


### 题目 68

题目：
使用生成器编写程序。当 n 通过控制台输入时，以逗号分隔的形式输出 0 到 n 之间的所有偶数。

示例：
若输入 n 为：

10

则输出应为：

0,2,4,6,8,10

提示：
使用 `yield` 生成生成器中的下一个值。
题目中给出的输入数据均视为通过控制台输入。


参考答案：

```python
def EvenGenerator(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1


n=int(input())
values = []
for i in EvenGenerator(n):
    values.append(str(i))

print(",".join(values))
```


### 题目 69

题目：
使用生成器编写程序。当 n 通过控制台输入时，以逗号分隔的形式输出 0 到 n 之间所有同时能被 5 和 7 整除的数。

示例：
若输入 n 为：

100

则输出应为：

0,35,70

提示：
使用 `yield` 生成生成器中的下一个值。
题目中给出的输入数据均视为通过控制台输入。


参考答案：

```python
def NumGenerator(n):
    for i in range(n+1):
        if i%5==0 and i%7==0:
            yield i

n=int(input())
values = []
for i in NumGenerator(n):
    values.append(str(i))

print(",".join(values))
```


### 题目 70

题目：
编写断言语句，验证列表 `[2,4,6,8]` 中的每个数字都是偶数。

提示：
使用 `assert 表达式` 进行断言。


参考答案：

```python
li = [2,4,6,8]
for i in li:
    assert i%2==0
```


### 题目 71

题目：
编写一个程序，从控制台接收一个基本数学表达式并输出其计算结果。

示例：
若输入字符串为：

35+3

则输出应为：

38

提示：
使用 `eval()` 计算表达式。


参考答案：

```python
expression = raw_input()
print(eval(expression))
```


### 题目 72

题目：
编写一个二分查找函数，在有序列表中查找某个元素。函数应返回该元素在列表中的索引。

提示：
使用 `if/elif` 处理不同条件。


参考答案：

```python
import math
def bin_search(li, element):
    bottom = 0
    top = len(li)-1
    index = -1
    while top>=bottom and index==-1:
        mid = int(math.floor((top+bottom)/2.0))
        if li[mid]==element:
            index = mid
        elif li[mid]>element:
            top = mid-1
        else:
            bottom = mid+1

    return index

li=[2,5,7,9,11,17,222]
print(bin_search(li,11))
print(bin_search(li,12))
```


### 题目 73

题目：
编写一个二分查找函数，在有序列表中查找某个元素。函数应返回该元素在列表中的索引。

提示：
使用 `if/elif` 处理不同条件。


参考答案：

```python
import math
def bin_search(li, element):
    bottom = 0
    top = len(li)-1
    index = -1
    while top>=bottom and index==-1:
        mid = int(math.floor((top+bottom)/2.0))
        if li[mid]==element:
            index = mid
        elif li[mid]>element:
            top = mid-1
        else:
            bottom = mid+1

    return index

li=[2,5,7,9,11,17,222]
print(bin_search(li,11))
print(bin_search(li,12))
```


### 题目 74

题目：
使用 Python 的随机数模块生成一个 10 到 100 之间的随机浮点数。

提示：
使用 `random.random()` 生成 `[0,1]` 范围内的随机浮点数。


参考答案：

```python
import random
print(random.random()*100)
```


### 题目 75

题目：
使用 Python 的随机数模块生成一个 5 到 95 之间的随机浮点数。

提示：
使用 `random.random()` 生成 `[0,1]` 范围内的随机浮点数。


参考答案：

```python
import random
print(random.random()*100-5)
```


### 题目 76

题目：
使用 `random` 模块和列表推导式，随机输出一个 0 到 10 之间（包含两端）的偶数。

提示：
使用 `random.choice()` 从列表中随机选择一个元素。


参考答案：

```python
import random
print(random.choice([i for i in range(11) if i%2==0]))
```


### 题目 77

题目：
使用 `random` 模块和列表推导式，随机输出一个指定范围内同时能被 5 和 7 整除的数。原文题目写的是 0 到 10 之间（包含两端）。

提示：
使用 `random.choice()` 从列表中随机选择一个元素。


参考答案：

```python
import random
print(random.choice([i for i in range(201) if i%5==0 and i%7==0]))
```


### 题目 78

题目：
编写一个程序，生成一个包含 5 个随机数的列表，随机数范围为 100 到 200（包含两端）。

提示：
使用 `random.sample()` 生成随机值列表。


参考答案：

```python
import random
print(random.sample(range(100), 5))
```


### 题目 79

题目：
编写一个程序，随机生成一个包含 5 个偶数的列表，这些偶数位于 100 到 200 之间（包含两端）。

提示：
使用 `random.sample()` 生成随机值列表。


参考答案：

```python
import random
print(random.sample([i for i in range(100,201) if i%2==0], 5))
```


### 题目 80

题目：
编写一个程序，随机生成一个包含 5 个数字的列表，这些数字位于 1 到 1000 之间（包含两端），并且同时能被 5 和 7 整除。

提示：
使用 `random.sample()` 生成随机值列表。


参考答案：

```python
import random
print(random.sample([i for i in range(1,1001) if i%5==0 and i%7==0], 5))
```


### 题目 81

题目：
编写一个程序，随机输出一个 7 到 15 之间（包含两端）的整数。

提示：
使用 `random.randrange()` 生成指定范围内的随机整数。


参考答案：

```python
import random
print(random.randrange(7,16))
```


### 题目 82

题目：
编写一个程序，对字符串 `hello world!hello world!hello world!hello world!` 进行压缩和解压缩。

提示：
使用 `zlib.compress()` 和 `zlib.decompress()` 压缩与解压字符串。


参考答案：

```python
import zlib
s = b'hello world!hello world!hello world!hello world!'
t = zlib.compress(s)
print(t)
print(zlib.decompress(t))
```


### 题目 83

题目：
编写一个程序，输出执行 100 次 `1+1` 所需的运行时间。

提示：
使用 `timeit()` 函数测量运行时间。


参考答案：

```python
from timeit import Timer
t = Timer("for i in range(100):1+1")
print(t.timeit())
```


### 题目 84

题目：
编写一个程序，将列表 `[3,6,7,8]` 随机打乱后输出。

提示：
使用 `shuffle()` 函数打乱列表。


参考答案：

```python
from random import shuffle
li = [3,6,7,8]
shuffle(li)
print(li)
```


### 题目 85

题目：
编写一个程序，将列表 `[3,6,7,8]` 随机打乱后输出。

提示：
使用 `shuffle()` 函数打乱列表。


参考答案：

```python
from random import shuffle
li = [3,6,7,8]
shuffle(li)
print(li)
```


### 题目 86

题目：
编写一个程序，生成所有可能的句子组合，其中主语来自 `["I", "You"]`，动词来自 `["Play", "Love"]`，宾语来自 `["Hockey", "Football"]`。

提示：
使用 `list[index]` 形式访问列表中的元素。


参考答案：

```python
subjects=["I", "You"]
verbs=["Play", "Love"]
objects=["Hockey","Football"]
for i in range(len(subjects)):
    for j in range(len(verbs)):
        for k in range(len(objects)):
            sentence = "%s %s %s." % (subjects[i], verbs[j], objects[k])
            print(sentence)
```


### 题目 87

题目：
编写一个程序，删除列表 `[5,6,77,45,22,12,24]` 中的所有偶数并输出结果。

提示：
使用列表推导式批量删除或筛选列表元素。


参考答案：

```
li = [5,6,77,45,22,12,24]
li = [x for x in li if x%2!=0]
print(li)
```


### 题目 88

题目：
使用列表推导式，删除列表 `[12,24,35,70,88,120,155]` 中能被 5 和 7 整除的数字，然后输出结果。

提示：
使用列表推导式批量删除或筛选列表元素。


参考答案：

```
li = [12,24,35,70,88,120,155]
li = [x for x in li if x%5!=0 and x%7!=0]
print(li)
```


### 题目 89

题目：
使用列表推导式，删除列表 `[12,24,35,70,88,120,155]` 中索引为 0、2、4、6 的元素，然后输出结果。

提示：
使用列表推导式批量删除或筛选列表元素。
使用 `enumerate()` 获取 `(索引, 值)` 元组。


参考答案：

```python
li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i%2!=0]
print(li)
```


### 题目 90

题目：
使用列表推导式生成一个 `3 × 5 × 8` 的三维数组，其中每个元素均为 0。

提示：
使用列表推导式创建数组。


参考答案：

```
array = [[ [0 for col in range(8)] for col in range(5)] for row in range(3)]
print(array)
```


### 题目 91

题目：
使用列表推导式，删除列表 `[12,24,35,70,88,120,155]` 中索引为 0、4、5 的元素，然后输出结果。

提示：
使用列表推导式批量删除或筛选列表元素。
使用 `enumerate()` 获取 `(索引, 值)` 元组。


参考答案：

```python
li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i not in (0,4,5)]
print(li)
```


### 题目 92

题目：
使用列表推导式，删除列表 `[12,24,35,24,88,120,155]` 中所有值为 24 的元素，然后输出结果。

提示：
可以使用列表的 `remove` 方法删除某个值；参考答案则使用列表推导式筛选。


参考答案：

```python
li = [12,24,35,24,88,120,155]
li = [x for x in li if x!=24]
print(li)
```


### 题目 93

题目：
给定两个列表 `[1,3,6,78,35,55]` 和 `[12,24,35,24,88,120,155]`，编写程序生成一个包含两者交集元素的列表。

提示：
使用 `set()` 和 `&=` 执行集合交集运算。


参考答案：

```python
set1=set([1,3,6,78,35,55])
set2=set([12,24,35,24,88,120,155])
set1 &= set2
li=list(set1)
print(li)
```


### 题目 94

题目：
给定列表 `[12,24,35,24,88,120,155,88,120,155]`，编写程序删除其中的所有重复值，同时保留原始顺序，并输出结果。

提示：
使用 `set()` 存储不重复的值。


参考答案：

```python
def removeDuplicate( li ):
    newli=[]
    seen = set()
    for item in li:
        if item not in seen:
            seen.add( item )
            newli.append(item)

    return newli

li=[12,24,35,24,88,120,155,88,120,155]
print(removeDuplicate(li))
```


### 题目 95

题目：
定义一个 `Person` 类及其两个子类 `Male` 和 `Female`。所有类都包含 `getGender` 方法：`Male` 类返回或输出 `Male`，`Female` 类返回或输出 `Female`。

提示：
使用 `子类(父类)` 的形式定义子类。


参考答案：

```python
class Person(object):
    def getGender( self ):
        return "Unknown"

class Male( Person ):
    def getGender( self ):
        return "Male"

class Female( Person ):
    def getGender( self ):
        return "Female"

aMale = Male()
aFemale= Female()
print(aMale.getGender())
print(aFemale.getGender())
```


### 题目 96

题目：
编写一个程序，统计并输出通过控制台输入的字符串中每个字符出现的次数。

示例：
若输入字符串为：

abcdefgabc

则输出应为：

a,2
c,2
b,2
e,1
d,1
g,1
f,1

提示：
使用字典存储键值对。
使用 `dict.get()` 方法查找键，并为不存在的键提供默认值。


参考答案：

```python
dic = {}
s=raw_input()
for s in s:
    dic[s] = dic.get(s,0)+1
print('\n'.join(['%s,%s' % (k, v) for k, v in dic.items()]))
```


### 题目 97

题目：
编写一个程序，从控制台接收一个字符串并将其逆序输出。

示例：
若输入字符串为：

rise to vote sir

则输出应为：

ris etov ot esir

提示：
使用 `list[::-1]` 或字符串切片以逆序方式遍历序列。


参考答案：

```python
s=raw_input()
s = s[::-1]
print(s)
```


### 题目 98

题目：
编写一个程序，从控制台接收一个字符串并输出索引为偶数的字符。

示例：
若输入字符串为：

H1e2l3l4o5w6o7r8l9d

则输出应为：

Helloworld

提示：
使用 `[::2]` 以步长 2 遍历序列。


参考答案：

```python
s=raw_input()
s = s[::2]
print(s)
```


### 题目 99

题目：
编写一个程序，输出列表 `[1,2,3]` 的所有排列。

提示：
使用 `itertools.permutations()` 获取列表的全排列。


参考答案：

```python
import itertools
print(list(itertools.permutations([1,2,3])))
```


### 题目 100

题目：
编写一个程序，解决经典的中国古代“鸡兔同笼”问题：

农场中鸡和兔共有 35 个头、94 条腿。请问鸡和兔各有多少只？

提示：
使用 `for` 循环遍历所有可能的解。


参考答案：

```python
def solve(numheads,numlegs):
    ns='No solutions!'
    for i in range(numheads+1):
        j=numheads-i
        if 2*i+4*j==numlegs:
            return i,j
    return ns,ns

numheads=35
numlegs=94
solutions=solve(numheads,numlegs)
print(solutions)
```
