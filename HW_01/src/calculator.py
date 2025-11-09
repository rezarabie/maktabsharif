
num1=float(input("plz input your first number  :"))
num2=float(input("plz input your second number :"))

opt=input("plz input the operand")



if(opt=="/" and num2==0):
   while True:
    num2=float(input("second number could not be zero :"))
    if(num2!=0):
        break
    else:
        continue



match opt:
    case "+":
       result=num1 + num2
    case "-":
       result=num1 - num2
    case "*":
       result=num1 * num2
    case "/":
       result=num1 // num2

print(f"{num1}{opt}{num2} ={result}" )

