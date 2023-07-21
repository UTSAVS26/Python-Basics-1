userInput = input("Write a sentence: ")
totalChar = len(userInput)
print("Total Characters: ",totalChar)
totalAlpha = totalDigit = totalSpecial = 0
for a in userInput:
    if a.isalpha():
        totalAlpha += 1
    elif a.isdigit():
        totalDigit += 1
    else:
        totalSpecial += 1
print("Total Alphabets: ",totalAlpha)
print("Total Digits: ",totalDigit)
print("Total Special Characters: ",totalSpecial)
totalSpace = 0
for b in userInput:
    if b.isspace():
        totalSpace += 1
print("Total Words in the Input :",(totalSpace + 1))
