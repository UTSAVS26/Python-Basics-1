# A python program to demonstrate the use of
# cmp(), max(), min()

tuple1 = ('python', 'geek')
tuple2 = ('coder', 1)

if (cmp(tuple1, tuple2) != 0):

     # cmp() returns 0 if matched, 1 when not tuple1
     # is longer and -1 when tuple1 is shoter
     print('Not the same')
else:
     print('Same')
print ('Maximum element in tuples 1,2: ' +
       str(max(tuple1)) + ',' +
       str(max(tuple2)))
print ('Minimum element in tuples 1,2: ' +
       str(min(tuple1)) + ',' + str(min(tuple2)))
