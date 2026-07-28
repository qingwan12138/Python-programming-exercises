# class 类名:
#     # 构造方法（初始化）
#     def __init__(self, 参数):
#         # 实例属性
#         self.属性 = 参数
#
#     # 实例方法
#     def 方法名(self):
#         方法逻辑
#

class InputOutString:
    def __init__(self):
        self.s = ""

    def getString(self):
        print("请输入字符串")
        self.s = input()

    def printString(self):
        print(self.s.upper())


strObj = InputOutString()
strObj.getString()
strObj.printString()
