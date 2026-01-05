def fun(n,s="(y)"):
    l=[]
    if n==0:
        return [s];
    else:
        for i in range(len(s)):
            if s[i]=='y':
                ns=s[0:i]+"(y)x(y)"+s[i+1:]
                l+=(fun(n-1,ns))
        return l
n=int(input("Enter no of nodes"))
lis=list(set(fun(n)))  #repeatation in result as it will generate same output for ambigous replacement of y (same structure diffenrent order replacement of y)
#can be avoided by using set inside the function to reduce the time complexity
for i in range(len(lis)):
    lis[i]=lis[i].replace("(y)","")
    
    for j in range(1,n+1):
        lis[i]=lis[i].replace("x",str(j),1)

        
    print(lis[i])
print("\ncount:",len(lis))
