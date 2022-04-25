import math


def get_last_digits_from_binary(value, num_of_dig):
    mask = (1 << num_of_dig) - 1
    bits = value & mask
    return bits

def get_first_digits_from_binary(value, num_of_dig):
    bits = value >> num_of_dig
    return bits
     
def add_bits(byte, bits, bits_num):
    shift = byte << bits_num
    nbyte = shift | bits
    return nbyte

def cut_bits(bits, num_to_remove, to_add):
    bits_to_remove = get_last_digits_from_binary(bits, num_to_remove)
    nbits = get_first_digits_from_binary(bits, num_to_remove)
    return bin(nbits)[2:].zfill(to_add), bin(bits_to_remove)[2:].zfill(num_to_remove)

def bit_combo(byte, bits, bits_num, lenb):
    if lenb + bits_num <= 8:
        nbyte = add_bits(byte, bits, bits_num)
        nlenb = lenb + bits_num
        return nbyte, nlenb, 0, 0
    else:
        bits_to_add = 8 - lenb
        bits_to_remove = bits_num - bits_to_add
        cut_bits_ = cut_bits(bits, bits_to_remove, bits_to_add)
        nbits = int(cut_bits_[0], 2)
        bits_removed = cut_bits_[1]
        nbyte = add_bits(byte, nbits, bits_to_add)
        return nbyte, 8, bits_to_remove, bits_removed

def create_byte(list, l):
    init_byte = bit_combo(int(list[0], 2), int(list[1], 2), l, l)
    byte = init_byte
    th = 1
    while byte[1] < 8 and th < len(list) - 1:
        th += 1
        k = bin(byte[0])[2:].zfill(byte[1])
        byte = bit_combo(int(k, 2), int(list[th], 2), l, byte[1])
    return byte

def bitlist_to_bytes(list, l): #not ready yet, under construction 
    elements_to_add = math.ceil(8 / l) 
    print(elements_to_add)
    bytelist = []
    bitlist = list[0:elements_to_add]
    print(bitlist)
    while not parsed:
        cr_byte = create_byte(bitlist, l)
        byte = bin(cr_byte[0])[2:].zfill(8)
        bytelist.append(byte)
        print(bytelist)
        if cr_byte[2] > 0: 
            print ('xxx')
            print(cr_byte)
            bits_left = cr_byte[3].zfill(cr_byte[2])
            print('bits left')
            print('xxxx')
            print(bits_left)
            bitlist = []
            bitlist.append(bits_left)
            #bitlist.append(????) 
        parsed = True
    return bitlist
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
