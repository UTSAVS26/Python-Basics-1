a=[[1,2,3],[2,3,4],[3,4,5]]
for x in range(0,3):
     for y in range(0,3):
          if (a[x][y]%2==1):
               print(a[x][y],end="\t")
          else:
               print(" ",end="\t")
     print()
