from os import system
import binascii

# print(binascii.hexlify(b'1'))
# Python3 program to illustrate 
# hex() function 
  
# print("The hexadecimal form of 23 is"
#                             + hex(15)) 
                              
# print("The hexadecimal form of the "
#       "ascii value is 'a' is " + hex(ord('a'))) 
        
# print("The hexadecimal form of 3.9 is "
#                         + float.hex(3.9)) 



# hex_string = "0x616263"[2:]
# # bytes_object = bytes.fromhex(hex_string)
# bytes_object =fromhex(hex_string)
# print(bytes_object)
# ascii_string = bytes_object.decode("ASCII")
# print(ascii_string)


# encoding string  
str_enc = str.encode('base64', 'strict') 
  
# printing the encoded string 
print ("The encoded string in base64 format is : ",str_enc)