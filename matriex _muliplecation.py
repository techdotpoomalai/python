import numpy as mat

def mul(a,b):
    mat1=a 
    mat2=b
    x=mat1.itemsize
    print(x)

# def shaps(a,b):
#     a_2d=mat.reshape(a,(2,2))
#     b_2d=mat.reshape(b,(2,2))
#     print(a_2d)
#     print(b_2d)
#     mul(a_2d,b_2d)

def cheak_lenth(a,b):
    if(a.itemsize==b.itemsize):
        print("Array size are equal")
        mul(a,b)
        # return(g)
    else:
        print("Array size are not equal")
        pass

a=mat.array([1,1,1,1,1,1,1,1,1],dtype=mat.int)
b=mat.array([2,2,2,2,2,2,2,2,],dtype=mat.int)
# c=mat.array([],dtype=mat.int16)
cheak_lenth(a,b)
# print(h)



