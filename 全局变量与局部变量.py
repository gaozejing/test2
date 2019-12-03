#全局变量与局部变量
global my_price#在外面不影响里面
def calculateTax(price,tax_rate):
    tatol = price + (price * tax_rate)
    global my_price#在里面会影响外面
    my_price = 10000
    print("my_price (inside function) = ",my_price)
    return tatol
my_price = float(input("Enter price : "))
total_price = calculateTax(my_price,0.06)
print("price = ",my_price,"Total price = ",total_price)
print("my_price(outside function) = ",my_price)