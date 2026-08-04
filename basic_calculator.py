#basic calculator
import sys #to invoke sys.exit() to end the program later on
print("Welcome to basic calculator program") #welcome statement
#creating two variables to accept and store numbers which would be entered by the user for the operation which they want to perform
a = int(input("Enter the first number you want to use for an operation :"))
b = int(input("Enter the second number :"))
#creating a variable to accept the respective sign of the operation which the user wants to perform
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
 print("Unidentified operator/character, reset the program") #for when user inputs an unmentioned sign or something unnecesary
 sys.exit() #to stop the program
