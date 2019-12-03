#创建一个空字典
Dictionary = {}
#假设这个添加词典操作可以循环100次
for i in range(100):
    Choose = input("Add or look up a word (a/l)? ")
    if Choose == "a":
        word = input("Type the word: ")
        definition = input("Type the definition: ")
        #将key和value放进字典
        Dictionary[word] = definition
        print("Word added")
        continue
    elif Choose == "l":
        word = input("Type the word: ")
        if word in Dictionary:
            #输出key对应的value
            print(Dictionary[word])
        else:
            print("That word isn't in the dictionary yet.")
        continue
    else:
        break

