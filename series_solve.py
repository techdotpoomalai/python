from os import system


def int_val(p):
    int_val=int(p)
    return(int_val)

def genral_term(a,d,n):
    result=a+(n-1)*d
    return(result)   

def add_nth_term(a,d,n):
    res=(2*a+(n-1)*d)*(n/2)
    return(res)

# sequence and series four type thir are Arirhmetic,Geometric,Hormonic and Fibonacci serius


#Arthmatic serius

#  ex. 2+4+6+8...n      in genral form:     a,a+2d,a+3d,...,a+(n-1)d,...
#Common diffrence or ratio=Successive term – Preceding term,        Common difference = d = a2 – a1
#General Term (n th Term)	A(n) = a + (n-1)d
#nth term from the last term	A(n) = l – (n-1)d
#Sum of first n terms	S(n) = n/2 (2a + (n-1)d)

system("cls")


print("\nYou want to sequence or sequence information?")
print("\nyou need a sequence just type 'seq' or sequence information 'seq_info'")
Input=input("\nEnter your key word:\t")
if Input=="seq":
    x,y,z=map(int,input("\nEnter 'start element', 'end element' and 'common differnces'\t").split(" ")) 
    print("Your sequence is now:\t",end="")
    for seq in range(x,y,z):
        print(seq,end="+")
    print("...",end="")
    print()
elif Input=="seq_info":
    series1=input("Enter your series e.x 1,2,3,...,n;\t")
    n=int(input("Enter limit:\t"))
    # series1="2,4,6,8,10,...,n"
    x1=series1.split(',')
    x1=x1[0:len(x1)-2]
    list_=[]
    for ele in x1:
        ele=int_val(ele)
        list_.append(ele)
    com_diff=list_[2]-list_[1]
    Nth_ele=genral_term(list_[0],com_diff,n)
    # print("\nCommon differnce of sequence d=",com_diff)
    print("\n The N th element is A(n)=",Nth_ele)
    add_nthterm=add_nth_term(list_[0],com_diff,n)
    print("\nSum of first to n th element:\t S(n)=",add_nthterm)
else:
    print("Your enter wrong input please enter valied input...!")


