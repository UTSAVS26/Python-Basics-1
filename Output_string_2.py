MyText="ApEACeDriVE"
ch="@"
l=len(MyText)
Msg=""
print("\n Orignal : ",MyText)
for cnt in range (l):
    if MyText[cnt]>='B' and MyText[cnt]<='G':
        Msg+=MyText[cnt].lower()
    elif MyText[cnt]=='A' or MyText[cnt]=='a':
        Msg+=ch;
    else:
        if(cnt%2==0):
            Msg+=MyText[cnt].upper()
        else:
            Msg+=MyText[cnt-1]
print("Final :",Msg)
