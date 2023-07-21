import math
hex = input("Enter a Hexadecimal Value: ")
oct = ""
dec = i = 0
c = len(hex) - 1
while i < len(hex):
     d = hex[i]
     if d == '0' or d == '1' or d == '2' or d == '3' or d == '4' or d == '5':
          dec = dec + int(d) * int(math.pow(16, c))
     elif d == '6' or d == '7' or d == '8' or d == '9':
          dec = dec + int(d) * int(math.pow(16, c))
     elif (d == 'A') or (d == 'a'):
          dec = dec + 10 * int(math.pow(16, c))
     elif (d == 'B') or (d == 'b'):
          dec = dec + 11 * int(math.pow(16, c))
     elif (d == 'C') or (d == 'c'):
          dec = dec + 12 * int(math.pow(16, c))
     elif (d == 'D') or (d == 'd'):
          dec = dec + 13 * int(math.pow(16, c))
     elif (d == 'E') or (d == 'e'):
          dec = dec + 14 * int(math.pow(16, c))
     elif (d == 'F') or (d == 'f'):
          dec = dec + 15 * int(math.pow(16, c))
     else:
          print("invalid input")
          break
     i+= 1
     c -= 1
while (dec > 0):
     oct = "".join([str(int(dec % 8)) , oct])
     dec = int(dec / 8)
print(hex,":",oct)
