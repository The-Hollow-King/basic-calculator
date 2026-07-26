#basic calculator
import sys
print("Welcome to basic calculator program")
a = int(input("Enter the first number you want to use for an operation :"))
b = int(input("Enter the second number :"))
q = input("Input the sign of the operator you want to use for the operation(+ , - , / , * , // , %):")
if(q == "+" or q == "-") or (q == "/" or q == "*") or (q == "//" or q == "%"):
 print ("Appropriate operator is used")
if(q == "+") :
 c = a + b
 print ("Answer :", c)
if(q == "-") :
 c = a - b
 print ("Answer :", c)
elif(q == "/") :
 c = a / b
 print ("Answer :", c)
elif(q == "*") :
 c = a * b
 print ("Answer :", c)
elif(q == "//") :
 c = a // b
 print ("Answer :", c)
elif(q == "%") :
 c = a % b
 print ("Answer :", c)
else :
 print("Unidentified operator/character, reset the program")
 sys.exit()
