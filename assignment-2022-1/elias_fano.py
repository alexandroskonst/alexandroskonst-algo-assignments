import math


def get_last_digits_from_binary(value, num_of_dig):
    mask = (1 << num_of_dig) - 1
    bits = value & mask
    return bits

def get_first_digits_from_binary(value, num_of_dig):
    bits = value >> num_of_dig
    return bits

def bit_combo(value1, value2, l, lenb):
    if lenb + l <= 8:
        fvalue = (value1 << l) | value2
    else:
        rem_bits = l - 8 - lenb
        

#get_first_digits_from_binary(0b0010011101, 2)
sorted_list = [5, 8, 11, 20, 33]

n = len(sorted_list)
m = max(sorted_list)

# l is the number of last digits
x = math.log2(m/n)
l = math.floor(x)

# u is the number of remaining digits
y = math.log2(m)
u = math.ceil(y) - l


# u + l is the number of bits that represent each integer
num_of_bits = int(l + u)
#print(num_of_bits)

#list to bytearray: the bytearray function receives a string or a collection of integers in the range 0-255 as input.
#the list cannot be converted to bytearray direclty (unless it is a string?)

#convert int to binary
binary_list = []
for i in sorted_list:
    binary_list.append(bin(i)[2:].zfill(num_of_bits))
print(binary_list)

#get last l digits from each binary and save to bytearray
Llist = []
for i in binary_list:
    Llist.append(bin(get_last_digits_from_binary(int(i), l))[2:].zfill(l))
print(Llist)

mod_bits = len(Llist) * 1 % 8
zero_to_add = 0
if mod_bits != 0:
    zero_to_add = 8 - mod_bits

#get first u digits and subtract from previous number
#U = bytearray()
Ulist = []
th = 0
for i in binary_list:
    if th == 0:
        ldig = get_first_digits_from_binary(int(i, 2), l)
        Ulist.append(ldig)
        th = 1
    else:
        ndig = get_first_digits_from_binary(int(i, 2), l)
        Ulist.append(ndig - ldig)
        ldig = ndig

print(Ulist)

test = [0b01000000, 0b01010101, 0b11001100, 0b00110011]
Ltest = bytearray(test)
for x in Ltest:
    print (bin(x)[2:].zfill(8))
