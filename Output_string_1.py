s=input("enter a string ")
count=3
while True:
    if s[0]=='a':
        s=s[2:]
    elif s[-1]=='b':
        s=s[:2]
    else:
        count = count+1
        break
print(s)
print(count)
