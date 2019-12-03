def calTotalCorn(Fcorn,Tcorn,Ocorn):
    #保留2位有效数字
    totalCorn = round(float(Fcorn)*0.5 + float(Tcorn)*0.2 +float(Ocorn)*0.1,2)
    print(totalCorn)

F = input("Five Corn: ")
T = input("Two Corn: ")
O = input("One Corn: ")
calTotalCorn(F,T,O)