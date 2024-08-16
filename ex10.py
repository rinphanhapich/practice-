#Ex10 - Number
#Enter 5 numbers and find maximum and minimum value
#Example:
# 1
# 5
# 6
# 7
# 0
# output : Max = 7, Min = 0
number=""
for i in range(5):
    n=input()
    number+=str(n)
    max_number=number
    min_number=number
    for i in range (len(number)):
        if number[i]>max_number:
            max_number = number[i]
        elif number[i]<min_number:
            min_number= number[i]
print("max_number",max_number)
print("min_number",min_number)