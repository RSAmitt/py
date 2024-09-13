#calculator

number1 = int(input("Enter Value:  "))
number2 = int(input("Enter Value:  "))
choose =input('choose one *,/,%,+,- : ')
if choose == '+' :
    print("Output is: ",number1 + number2)
elif choose == '-' :
    print("Output is: ",number1-number2)

elif choose == '*' :
    print("Output is: ",number1*number2)

elif choose == '/' :
    print("Output is: ",number1/number2)

elif choose == '%' :
    print("Output is: ",number1%number2)

else : 
    print('Enter Valid Operations')




