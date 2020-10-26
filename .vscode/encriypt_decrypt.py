from os import system
import binascii

def string(value):
    str_=""
    for arr in value:
        str_+=arr       # concatinate given string
    return(str_)

def string_convert(value_):
    temp=string(value_)
    x=int(temp)
    return(x)

def Encryption():
    encode=input("\nEnter encrypted word\n\n")      # Here two type of inputs thier are int type string type
    if type(encode)==int:                           # If is cheak int type 
        hide_data=hex(encode)                       # hex fuction converted acci to char 
        print("Encription now:%X",hide_data)
        print("\n")
    elif type(encode)==str:                         # elif is cheak string type
        hide_data_assci=[]
        temp_assci=[]
        Final_encode=[]
        Final_encode_=[]
        encode_str=encode
        for loop in encode_str:      
            hide_data_assci.extend(ord(num) for num in loop) # ord function char convert to ascci and extend function adding essence in string only
        for loop_ in hide_data_assci:
            Final_encode=hex(loop_)                 # Hex function convert int(ascii) to hexadacimal
            Final_encode_.append(Final_encode)
        print("\nEncryption now:",string(Final_encode_))    #call string function
        print("\n")
    else:
        pass

def Decryption():
    # global_input=input("If you need single decrypt type 'yes' otherwise 'No'\n\n")
    global_input="yes"
    local_input_split=[]
    output=[]
    output_=[]
    final_out_char=[]
    final_out_str=[]
    if global_input=="yes" or global_input=="Yes" or global_input=="YES":
        print("Note:This is ascii base decode\n")
        # local_input=input("\nEnter decrypt word:\t")
        local_input="0x970x98"                               #this is hex inputs tier char value a,b
        local_input_split=local_input.split('0x')            # split in '0x' place
        local_input_split_slice=local_input_split[1:]        # slice in first element
        # print(local_input_split_slice)
        for loop in local_input_split_slice:
            string=loop
            x=string_convert(string)                         #call string_convert fuction
            output.append(x)
        for _ in output:
            __=chr(_)
            final_out_char.append(__)
        string(final_out_char)
        print(final_out_char)
            
    elif global_input=="No" or global_input=="no" or global_input=="NO":
        print("\n\nThis is base 64 decryption\n\n")
        Mix_char=input("Enter decode code\n\n")
        Mix_char.encode('base64','strict')
        
    else:
        print("Other Decryption not available here")

system('cls')       # this is clear the screen function
print("\nWelcome to the encription and decrption\n")

# input_=input("Do you want to Encryption type in the 'Encrypt' or Decryption type 'Decrypt' \n")
input_="decrypt"
if input_=="encrypt" or input_=="Encrypt" or input_=="ENCRYPT":
    Encryption()        #call Encrypt function
elif input_=="decrypt" or input_=="Decrypt" or input_=="DECRYPT":
    Decryption()        #call decrypt function
else:
    print("\n\nYour Entered Incorrect Input plese 'Enter correct input'.\n\n")