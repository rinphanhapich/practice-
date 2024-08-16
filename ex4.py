#We have text = "3 4 5 6"
#Q1 - display number 1 by one without space
text = " 3 4 5 6"
count = 0
for i in range(len(text)):
    if text[i] !=" ":
        count += len(text[i])
print(count)
#Q2 - Sum all number (Total: 18)
text= "3 4 5 6"
result=0
for i in range(len(text)):
    if text[i]!=" ":
      result+=int(text[i])
print(result)