#Program to 
def deleteChar(string,char):
    newString = string.replace(char,'')
    return newString
userInput = input("Enter any string: ")
delete = input("Input the character to delete from the string: ")
newStr = deleteChar(userInput,delete)
print("The new string after deleting all occurrences of",delete,"is: ",newStr)
