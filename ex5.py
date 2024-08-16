
#Q2 - Sum all number 
text = "454639"
sum = 0
for i in range (len(text)):
        sum+=int(text[i])
print("sum all number",sum)
#Q1 - Count odd and even number in text
text = "454639"
count_even = 0
count_old = 0
for i in range (len(text)):
    if int(text[i]) %2 ==0:
        count_even+=1
    if int(text[i]) %2 ==1:
        count_old+=1
print("count all even number",count_even)
print("count all old number",count_old)

#Q3 - Sum only even number 
text = "454639"
count = 0
for i in range (len(text)):
    if int(text[i]) %2 ==0:
        count+=int(text[i])
print("sum all even number",count)
#Q4 - Reverse 
text = "454639"
result = " "
for i in range (len(text)):
    result +=(text[len(text)-1-i])
print(result)
