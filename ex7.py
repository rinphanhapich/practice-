#Ex7 - number
#Enter number in range 10 - 20 until you enter other number out of range
#display "Continue" if number in range 10 - 20
#display "Out of range" if number difference from range 10 - 20
number=input("Enter number: ")
result =" "
for i in range(len(number)):
    if int(number)> 10 and int(number)<20 :
        result="countinue"
    else:
        result="ount of range"
print(result)