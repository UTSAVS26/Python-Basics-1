d = {}
l_sub = []
for i in range(1,6):
    sub = input("Enter the name of subject no.%u: "%i)
    l_sub += [sub]
print()
for x in range(1,6):
    t_stu = ()
    roll = input("Enter the roll number of student %u: "%x)
    for i in l_sub:
        sub_mrks = float(input("Enter the marks in %s: "%i))
        t_stu += (sub_mrks,)
    d[roll] = t_stu
    print()
print("ROLL NO.  ",end = '')
for sub in l_sub:
    print("%s  "%sub.upper(),end ='\t')
print()
for roll,marks in d.items():
    print(roll,end = '\t')
    for mrk in marks:
        print(mrk,end = '\t\t')
    print()
print()
print()
print("ROLL NUMBER \t TOTAL MARKS")
for roll, marks in d.items():
    s = sum(marks)
    print(roll,' \t\t ',s)
