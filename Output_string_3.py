s=input("enter a string ")
while len(s)<=4:
    if s[-1]=='z':
        s=s[0:3]+'c'
    elif 'a' in s:
        s=s[0]+'bb'
    elif not int(s[0]):
        s='1'+s[1:]+'z'
    else:
        s=s+'*'
        break
print(s)
