import math 

def binaryToDecimal(binary):
     
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal   


sorted_list = [5, 8, 11, 20, 33]
n= len(sorted_list)
m = max(sorted_list)

x = math.log2(m/n)
l = math.floor(x)
binary_list = []
for i in sorted_list:
    binary_list.append(bin(i))
Last_digits = []
remaining_digits = []
for i in binary_list:
   Last_digits.append(i[-2:])
   remaining_digits.append(i[:-2])

to_decimal = []
for i in Last_digits:
   to_decimal.append(int(i,2))

#L = bytearray(to_decimal)
L = bytearray(int(Last_digits))
print (L)
print(binary_list)
print(Last_digits)
print(remaining_digits)

bytes_as_bits = ''.join(format(ord(byte), '08b') for byte in L)

#print(to_decimal)

#L = bytearray(Last_digits)

int_val = int.from_bytes(b'\x01', "big")


    
#print (int_val)
   
 





