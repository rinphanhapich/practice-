#Enter text and check if it contains capital letter or not
#Display "Yes" if capital
#display "No" if all lowercase letter
user_input = input("Input text: ")
isCapital = False
for i in range(len(user_input)):
    if user_input[i]==user_input[i].upper():
        isCapital = True
if isCapital:
    print("Yes")
else:
    print("No")