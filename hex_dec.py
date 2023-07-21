def hexadecimalToDecimal(hexnum):
     length = len(hexnum)
     base = 1
     dec_val = 0
     for i in range(length - 1, -1, -1):
          if hexnum[i] >= '0' and hexnum[i] <= '9':
               dec_val += (ord(hexnum[i]) - 48) * base
               base = base * 16
          elif hexnum[i] >= 'A' and hexnum[i] <= 'F':
               dec_val += (ord(hexnum[i]) - 55) * base
               base = base * 16
     return dec_val 
  
# Driver code
if __name__ == '__main__': 
    hexnum = input("Enter a Hexadecimal Value: ")
    print(hexnum,":",hexadecimalToDecimal(hexnum))
