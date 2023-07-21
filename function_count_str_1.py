#Function to count the number of times a character occurs in a string
def charCount(ch,st):
     count = 0
     for character in st:
          if character == ch:
               count += 1
     return count
#end of function

st = input("Enter a string: ")
ch = input("Enter the character to be searched: ")
count = charCount(ch,st)
print("Number of times character",ch,"occurs in the string is:",count)
