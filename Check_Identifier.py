import keyword
s=input("Enter valid identifier name: ")
if s.isidentifier() and not keyword.iskeyword(s):
     print("Valid Identifier")
else:
     print("Invalid Identifier")
