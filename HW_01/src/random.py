import random2 as random

TrueValue=random.randint(1,100)
number=int(input("plz input your number "))
    
while True:
    if(number==TrueValue):
        print("you succssed")
        break
    elif(number>TrueValue):
        print("large")
    elif(number<TrueValue):
        print("low")

    number=int(input("plz input your number "))