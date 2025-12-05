from numbers import Num

absVar = -5
#print(f'abs(absVal): {Num.abs(absVar)}')

powVal = 5
powExp = 2
#print(f'{powVal}^{powExp}: {Num.pow(powVal, powExp)}')

sqrtVal = 10.89
print(f'sqrt({sqrtVal}): {Num.sqrt(sqrtVal)}')
print(f'bin(33): {bin(33)}')

#print(f'bin(3.3): {bit(3.3)}')

'''
import struct

def float_to_binary(num):
    # Pack the float into a 4-byte (32-bit) binary string in big-endian format
    # '!' for network byte order (big-endian), 'f' for float
    packed = struct.pack('!f', num)
    
    # Unpack the binary string as an unsigned integer
    # 'I' for unsigned int
    integer_representation = struct.unpack('!I', packed)[0]
    
    # Format the integer as a 32-bit binary string with leading zeros
    binary_string = f"{integer_representation:032b}"
    
    return binary_string

# Example usage:
my_float = 3.3
binary_repr = float_to_binary(my_float)
print(f"The binary representation of {my_float} is  : {binary_repr}")

my_float_negative = 10.89
binary_repr_neg = float_to_binary(my_float_negative)
print(f"The binary representation of {my_float_negative} is: {binary_repr_neg}")
'''