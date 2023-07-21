def BinaryToWords(binary):
     binary1 = binary  
     words, i, n = 0, 0, 0
     while(binary != 0):
          dec = binary % 10
          words = words + dec * pow(2, i)  
          binary = binary//10
          i += 1
     return (words)     
  
# Driver's code
bin_data = input('Enter any Binary number: ')
print("The binary value is:", bin_data)
str_data =' '
for i in range(0, len(bin_data), 7):
     temp_data = int(bin_data[i:i + 7])
     words_data = BinaryToWords(temp_data)
     str_data = str_data + chr(words_data)  
print("The Binary value after string conversion is:",str_data)
