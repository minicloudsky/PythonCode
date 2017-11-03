#coding: utf-8
import sys
num = []
for i in range(100):
        if i%8 ==0:
                num.append(i)
while True :
        s = sys.stdin.readline()
        s = str(s)
        n=len(s)
        n-=1
        int_n=n//8
        left_n=n%8
        st=[]
        for i in range(n):
                st=
                
        if left_n!=0:
                tmpp='0'*(8-left_n)
                for i in range(8-left_n):
                    st.append(tmpp[i])

