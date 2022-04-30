from collections import OrderedDict

thatsALowPrice = 7.50
thatsAHighPrice = 10.50
thatsAHighPrice= 12.50
thatsAVeryHighPrice=15.00
myMenu = OrderedDict()

myMenu["Цезарь с курицей"] = thatsALowPrice
myMenu["Цезарь с креветками"] = thatsALowPrice
myMenu["Jack Danie'ls"] =thatsAVeryHighPrice
myMenu["Vine"]=thatsALowPrice
myMenu["Стейк"]=thatsAVeryHighPrice


i=1
for k, v in myMenu.items():
    print(i, ":", k, "\t\t", v)
    i+=1

itemNumber = int(input("Choose your item: "))
item=list(myMenu.items())[itemNumber-1]

print("You chose", item[0], "at a price of: $"+str(item[1]))