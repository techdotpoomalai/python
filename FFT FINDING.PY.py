x1,x2,x3,x4,x5,x6,x7,x8=map(complex,input("Enter your inputs:").split())
# x1=0;x2=1;x3=2;x4=3;x5=4;x6=5;x7=6;x8=7;
# twittle factor w8,0=1,  w8,1=0.707-0.707j,  w8,2=-j,  w8,3=0.707+0.707,   w8,4=-1

# This is first stage
f1=x1+x4
f2=x1-x4
f3=x2+x6
f4=x2-x6
f5=x1+x5
f6=x1-x5
f7=x3+x7
f8=x3-x7

# This is second stage
s1=f1+f3
s2=f2+f4
s3=f1-f3
s4=(f2-f4)*(-1j)
s5=f5+f7
s6=f6+f8
s7=f5-f7
s8=(f6-f8)*(-1j)

# This is final stage
t1=s1+s5
t2=s2+s6
t3=s3+s7
t4=s4+s8
t5=s1-s5
t6=(s2-s6)*(0.707-0.707j)
t7=(s3-s7)*(-1j)
t8=(s4-s8)*(0.707+0.707j)
FFT=[]
FFT=[t1,t2,t3,t4,t5,t6,t7,t8]
print(FFT)
