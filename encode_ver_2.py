def convert(val):
    temp=[]
    for elf in val:
        elf_if=chr(elf)
        temp.extend(elf_if)
    return (temp)

def arrage(c):
    str=""
    for arr in c:
        str+=arr
    print(str)

print("This is example value:'qppnbmbj'")
encoded_word=str(input("Enter encoded word:"))
encript=input("Enter your encrpt value range:")
# encoded_word="cdef"
# encript=3
encode=[]
encode2=[]
encode_final=[]
gen_encod_list=[]
for ele in encoded_word:
    encode.extend(ord(num) for num in ele)
# print(encode)

for y in range(1,int(encript)+1):
    dummy = []
    for x in encode:
        dummy.append(x+y)
    encode2.append(dummy)
# print(encode2)

d=[]
dash=[]
for gh in encode2:
    d=convert(gh)
    dash.append(d)
# print(dash)

for c in dash:
    arrage(c)