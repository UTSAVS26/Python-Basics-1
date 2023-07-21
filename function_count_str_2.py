# Python Program - Count Number of Each Vowels
print("Enter 'x' for exit.");
str16 = input("Enter a String: ");
if str16 == 'x':
     import sys
     sys.exit()
else:
    vowels = 'aeiou'
    str16 = str16.casefold();
    count = {}.fromkeys(vowels,0);
    print();
    for char in str16:
         if char in count:
              count[char] += 1
print(count)
