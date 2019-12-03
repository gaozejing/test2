#建立一个空姓名列表
NameList = []
print("Enter 5 names:")
#在姓名列表内添加姓名
for i in range(5):
    name = input()
    NameList.append(name)
#输出姓名列表中的姓名
print("The names are ",end="")
for name in NameList:
    print(name+" ",end="")
print()
#对姓名列表进行排序操作，且不改变原来的列表
NameListCopy = NameList[:]
NameListCopy.sort()
print("NameList:",end="")
print(NameList)
print("NameList sort:",end="")
print(NameListCopy)
#输出原列表中的第三个姓名
print("The third name is: "+NameList[2])
#根据输入对原列表中的其中一个姓名进行替换
ReplayNameNum = int(input("Replace one name.Which one?(1-5):"))
ReplayName = input("New name: ")
NameList[ReplayNameNum-1] = ReplayName
print("The names are ",end="")
for name in NameList:
    print(name+" ",end="")