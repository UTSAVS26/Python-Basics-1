def emptylist():
    elist=[]
    print(elist)
def integerlist():
    intlist=[3,4,1,4,6,2,1,7,8,5,3,7,2,1,6,4,8,2,3,7,5]
    print(intlist)
def stringlist():
    strlist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    print(strlist)
def mixdlist():
    mxdlst=[2,'a',0,'b',3,' ']
    print(mxdlst)
def listfromstring():
    ln=list('saanvi')
    print(ln)
def interactivlist():
    intvlist=list(input('enter the remaining elements : '))
    print(intvlist)
def conctdlist():
    strlist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    intvlist=list(input('enter the remaining elements : '))
    cntdlst=strlist+intvlist
    print(cntdlst)
def lengthlist():
    intlist=[3,4,1,4,6,2,1,7,8,5,3,7,2,1,6,4,8,2,3,7,5]
    print(len(intlist))
def slicinglist():
    intlist=[3,4,1,4,6,2,1,7,8,5,3,7,2,1,6,4,8,2,3,7,5]
    print(intlist[5:-9])
    print(intlist[::5])
    print(intlist[4::])
    print(intlist[0:19:2])
def comparinglist():
    intlist=[3,4,1,4,6,2,1,7,8,5,3,7,2,1,6,4,8,2,3,7,5]
    intlist2=[2,1,4,7,6,1,4,6,8,9,1,6,4,7,8,1,2,5,4,7,1,3,5]
    print(intlist>intlist2)
def accessingitem():
    intlist2=[2,1,4,7,6,1,4,6,8,9,1,6,4,7,8,1,2,5,4,7,1,3,5]
    print(intlist2[9])
    print(intlist2[-9])
def traversinglist():
    intlist2=[2,1,4,7,6,1,4,6,8,9,1,6,4,7,8,1,2,5,4,7,1,3,5]
    for b in intlist2:
        print(b)
def replicatinglist():
    intlist=[3,4,1,4,6,2,1,7,8,5,3,7,2,1,6,4,8,2,3,7,5]
    print(intlist*2)
def membershptstng():
    list2=[3,4,1,4,6,2,1,7,8,5,3,7,2,1,6,4,8,2,3,7,5]
    for alphabets in list2:
        print(alphabets)
def appndngitm():
    name=['s','a','a','n','v','i']
    name.append('bhati')
    print(name)
def countfunc():
    name=['s','a','a','n','v','i']
    print(name.count('s'))
def indxnglist():
    intlist=[3,4,1,4,6,2,1,7,8,5,3,7,2,1,6,4,8,2,3,7,5]
    print(intlist[15])
def rmovefunc():
    name=['s','a','a','n','v','i']
    name.remove('i')
    print(name)
def delfunc():
    name=['s','a','a','n','v','i']
    del name[2]
    print(name)
def popfunc():
    name=['s','a','a','n','v','i']
    name.pop()
    print(name)
    name.pop(1)
    print(name)
def clringlist():
    intlist=[3,4,1,4,6,2,1,7,8,5,3,7,2,1,6,4,8,2,3,7,5]
    intlist.clear()
    print(intlist)
def serchnglist():
    name=['s','a','a','n','v','i']
    for s in name:
        print(name)
def extndinglist():
    list1=[3,4,1,4,6,2,1,7,8,5,3,7,2,1,6,4,8,2,3,7,5]
    list2=['s','a','a','n','v','i']
    list1.extend(list2)
    print(list1)
def indexfunc():
    list1=['s','a','a','n','v','i']
    print(list1.index('s'))
def insrtfunc():
    name=['s','a','a','n','v']
    name.insert (5,'i')
    print(name)
def updtingitm():
    ln=['s','a','a','n','v','i']
    ln[5]='B'
    print(ln)
def rvrselist():
    list1=['s','a','a','n','v','i']
    print(list1.reverse())
    print(list1)
def sortdfunc():
    namlist=['s','a','a','n','v','i']
    print(sorted(namlist))
def sortfunc():
    namlist=['s','a','a','n','v','i']
    namlist.sort()
    print(namlist)
def maxfunc():
    numlist=[3,4,1,4,6,2,1,7,8,5,3,7,2,1,6,4,8,2,3,7,5]
    print(max(numlist))
def minfunc():
    numlist=[3,4,1,4,6,2,1,7,8,5,3,7,2,1,6,4,8,2,3,7,5]
    print(min(numlist))
def sumfunc():
    numlist=[3,4,1,4,6,2,1,7,8,5,3,7,2,1,6,4,8,2,3,7,5]
    print(sum(numlist))
print("1. empty list")
print("2. integer list")
print("3. string list")
print("4. mixed list")
print("5. list from string")
print("6. interactive list")
print("7. concatenation of list")
print("8. length of list")
print("9. slicing list")
print("10. comparing list")
print("11. accessing items in a list")
print("12. traversing a list")
print("13. replicating a list")
print("14. membership testing")
print("15. appending item in a list")
print("16. count function in a list")
print("17. indexing in a list")
print("18. removing an item in list")
print("19. deleting an item in list")
print("20. pop function in a list")
print("21. clearing a list")
print("22. searching in a list")
print("23. extending a list")
print("24. index function in a list")
print("25. inserting an element in the list")
print("26. updating an element in list")
print("27. reversing a list")
print("28. sorted function in a list")
print("29. sort function in list")
print("30. max function in list")
print("31. min function in list")
print("32. sum function in list")
choice=0
while choice<=35:
    choice=int(input("enter your choice : "))
    if choice==1:
        emptylist()
    elif choice==2:
        integerlist()
    elif choice==3:
        stringlist()
    elif choice==4:
        mixdlist()
    elif choice==5:
        listfromstring()
    elif choice==6:
        interactivlist()
    elif choice==7:
        conctdlist()
    elif choice==8:
        lengthlist()
    elif choice==9:
        slicinglist()
    elif choice==10:
        comparinglist()
    elif choice==11:
        accessingitem()
    elif choice==12:
        traversinglist()
    elif choice==13:
        replicatinglist()
    elif choice==14:
        membershptstng()
    elif choice==15:
        appndngitm()
    elif choice==16:
        countfunc()
    elif choice==17:
        indxnglist()
    elif choice==18:
        rmovefunc()
    elif choice==19:
        delfunc()
    elif choice==20:\
        popfunc()
    elif choice==21:
        clringlist()
    elif choice==22:
        serchnglist()
    elif choice==23:
        extndinglist()
    elif choice==24:
        indexfunc()
    elif choice==25:
        insrtfunc()
    elif choice==26:
        updtingitm()
    elif choice==27:
        rvrselist()
    elif choice==28:
        sortdfunc()
    elif choice==29:
        sortfunc()
    elif choice==30:
       maxfunc()
    elif choice==31:
        minfunc()
    elif choice==32:
       sumfunc()
    else:
        print('invalid choice')
