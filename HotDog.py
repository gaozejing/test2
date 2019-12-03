class HotDog:
    #初始化实例
    def __init__(self):
        self.cooked_level = 0
        self.cooked_string = "Raw"
        self.condiments = []
    #优化实例输出
    def __str__(self):
        msg = "Hot Dog"
        if len(self.condiments) > 0:
            msg = msg + "with"
        for i in self.condiments:
            msg = msg + i + ", "
        msg = msg.strip(", ")#Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
        msg = self.cooked_string + " " + msg + "."
        return msg
    #用时间判断热狗的生熟
    def cook(self,time):
        self.cooked_level = self.cooked_level + time
        if self.cooked_level > 8:
            self.cooked_string = "Charcoal"
        elif self.cooked_level >5:
            self.cooked_string = "Well-done"
        elif self.cooked_level >3:
            self.cooked_string = "Medium"
        else:
            self.cooked_string = "Raw"
    #加入配料列表
    def addCondiment(self,condiment):
        self.condiments.append(condiment)

myDog = HotDog()
print(myDog)
print("Cooking hot dog for 4 minutes...")
myDog.cook(4)
print(myDog)
print("Cooking hot dog for 3 minutes...")
myDog.cook(3)
print(myDog)
print("Cooking hot dog for 10 minutes...")
myDog.cook(10)
print(myDog)
print("Now,I'm going to add some stuff on my hot dog")
myDog.addCondiment("ketchup")
myDog.addCondiment("mustard")
print(myDog)