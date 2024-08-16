#Ex6 - Number
#Enter number and check 
#if odd number print "Odd" otherwise print "Even"
number =input("Enter number: ")
for i in range(len(number)):
    if int(number[i]) %2 ==0:
        print("even")
    if int(number[i]) %2 ==1:
        print("old")
  