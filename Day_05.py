# 顺序表
# class A:
#     def func(self):
#         print("Hi")

# def monkey(self):
#     print("Hi, monkey")

# A.func = monkey
# a = A()
# a.func()

# mylist=[0,1,2,3,4,5,6,7,8]
# print(mylist[-3])
# print(mylist[-6:-1])


# for i in range(7):
#     if i==3: continue
#     print(i)

# fid = lambda n : n if n <= 2 else fid(n-1)+fid(n-2)

# istData = [fid(i) for i in range(1,10)]
# print(istData)

# print(fid(3))

# 顺序表一般存储相同数据类型

# 从起始地址 变量名指向起始地址  相同数据类型

# 字符串在内存中存储后面要加一个\0 多一位

# 地址是统一的 无论存字符串 还是整形 地址都站4个字符 
# 在存不同数据的时候它的占的字符是不一样的 但是都会有一个地址来存放的
# 所以我们可以用元素外置来把数据对应的地址 来连续的存储起来