def rotation(s,dir,no):
    c=0
    if dir=="l":
        inx=s.index(no)+len(no)
        for i in range(inx+1,len(s)+1):
            if s[i]==")":
                if c==0:
                    break
                else:
                    c-=1
            elif s[i]=="(":
                c+=1
        c2=0
        s2=s[:inx][::-1]
        for i2 in range(len(s2)):
            if s2[i2]=="(":
                if c2==0:
                    break
                else:
                    c2-=1
            elif s2[i2]==")":
                c2+=1
        i2=len(s2)-i2
#        print(s[inx],inx)
#        print(s)
        c3=0
        n0=""
        for i3 in s[inx:]:
            if c3 == 1:
                if i3 not in ["(",")"]:
                    n0+=i3
            if i3=="(":
                c3+=1
            elif i3==")":
                c3-=1
#        print(n0)
        i3=s.index(n0)
#        print(i,i3)

     #   for i in range(len(s2)):
     #       if 
     #i stopped here trying to add bracket adding
        
        ns=s[:i2]+"("+s[i2:inx]+s[inx+1:i3]+")"+s[i3:i]+s[i+1:]
        return ns        
    else: 
        inx=s.index(no)-1
        s2=s[:inx][::-1]
        for i in range(len(s2)):
            if s2[i]==")":
               c+=1
            elif s2[i]=="(":
                if c==0:
                    break
                else:
                    c-=1
        i=len(s2)-i-1
        c=0
        for i1 in range(inx+1,len(s)+1):
            if s[i1]==")":
                if c==0:
                    break
                else:
                    c-=1
            elif s[i1]=="(":
                c+=1

        c3=0
        s3=s[:inx+1][::-1]
#        print(s3[::-1])
        for i3 in range(len(s3)):
            n0=""
#            print(i3,s3[i3],c3)
            if s3[i3]==")":
               c3+=1
            elif s3[i3]=="(":
                c3-=1
            if c3==1:
                if s3[i3] not in ["(",")"]:
                   n0=s3[i3]+n0
                   break
        i2=s.index(n0)+len(n0)
        ns2=s[:i]+s[i+1:i2]+"("+s[i2:inx]+s[inx+1:i1]+")"+s[i1:]
#        print(s)
#        print(ns2)
#        ns=s[:i]+s[i+1:inx]+"("+s[inx+1:i1]+")"+s[i1:]
        return ns2
def checkrot(s,no):
    l=len(no)
    c1=s[s.index(no)-1]==")" #right rotation possible
    c2=s[s.index(no)+l]=="(" #left rotation possible
    if c1 and c2:
        i=input("Rotations available\n1:Right\n2:Left\nEnter choice:")
        if i=="1":
            return rotation(s,"r",no)
        elif i=="2":
            return rotation(s,"l",no)
        else:
            printf("invalid choice")
            return s
    elif c1: 
        i=input("Rotations available\n1:Right\nEnter choice:")
        if i=="1":
            return rotation(s,"r",no)
        else:
            printf("invalid choice")
            return s
    elif c2:
        i=input("Rotations available\n2:Left\nEnter choice:")
        if i=="2":
            return rotation(s,"l",no)
        else:
            printf("invalid choice")
            return s
    else:
        print("No rotation available at node")
        return s


    """
s="(((0)1(2))3((4)5))"
no="2"
#leftrot(s,no)
print(rotation(s,"l","3"))

"""  
n=int(input("Enter no nodes:"))
s="(1)"
for i in range(2,n+1):
    i1=s.index(")")
    s=s[:i1]+"("+str(i)+")"+s[i1:]
print(s)


while(True):
    no=input("Enter node to rotate at:")
    s=checkrot(s,no)
    print(s)
    c=input("Do you wish to continue?(y/n)\n")
    if c=="n":
        break
