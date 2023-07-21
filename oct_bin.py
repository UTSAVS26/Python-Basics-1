def OctToBin(octnum):
     binary = ""
     while octnum != 0:
          d = int(octnum % 10)
          if d == 0:
               binary = "".join(["000", binary])
          elif d == 1: 
               binary = "".join(["001", binary]) 
          elif d == 2:
               binary = "".join(["010", binary]) 
          elif d == 3:
               binary = "".join(["011", binary]) 
          elif d == 4:
               binary = "".join(["100", binary]) 
          elif d == 5: 
               binary = "".join(["101", binary]) 
          elif d == 6: 
               binary = "".join(["110",binary]) 
          elif d == 7: 
               binary = "".join(["111", binary]) 
          else: 
               binary = "Invalid Octal Digit"
               break
          octnum = int(octnum / 10) 
     return binary 
  
# Driver Code 
octnum = int(input("Enter a Octal Value: "))
final_bin = "" + OctToBin(octnum)
print(octnum,":", final_bin)
