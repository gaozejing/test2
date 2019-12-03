#函数的参数是列表
def printWorld (WordList=[]):
    for s in WordList:
        print(s)

name = input("name: ")
adr = input("adr: ")
street = input("street: ")
city = input("city: ")
province = input("province: ")
codenum = input("codenum: ")
country = input("country: ")

List = [name,adr,street,city,province,codenum,country]
printWorld(List)