#Ex8 - String
#We have text = "9394884039"
#Q1 - How many number 8 in string
text = "9394884039"
count_8=0
for i in range(len(text)):
    if text[i] == "8":
        count_8 +=1
print(count_8)
#Q2 - What is first index of letter 8
text = "9394884039"
position = 0
is_found=False
for i in range(len(text)):
    if int((text[i]) == "8") and not is_found:
        position= i
        is_found = True
print(position)
