import networkx as nx
import matplotlib.pylab as plt

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
        for i3 in range(inx,len(s)):
            if c3 == 1:
                if s[i3] not in ["(",")"]:
                    n0+=s[i3]
                    if s[i3+1] in ["(",")"]:
                        break
            if s[i3]=="(":
                c3+=1
            elif s[i3]==")":
                c3-=1
#        print(n0,no,dir)
#        print(s)
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
                    if s3[i3+1] in ["(",")"]:
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
        return [(s,rotation(s,"r",no)),(s,rotation(s,"l",no))]
    elif c1: 
        return [(s,rotation(s,"r",no))]
    elif c2:
        return [(s,rotation(s,"l",no))]
    else:
        return []
n=int(input("Enter no nodes:"))
s="(1)"
for i in range(2,n+1):
    i1=s.index(")")
    s=s[:i1]+"("+str(i)+")"+s[i1:]
edge_set=set()
vertex_set=set()
edge_list=[]
vertex_list=[] 
vertex_set.add(s)
tried_vertex=set()
remaning_vertex=set()
remaning_vertex.add(s)
while len(remaning_vertex)!=0:
    s=remaning_vertex.pop()
    #print("r:",remaning_vertex,"\ns:",tried_vertex)
    tried_vertex.add(s)
    for no in range(1,n+1):
        lst=checkrot(s,str(no))
        for i in lst:
            edge_set.add(i)
            vertex_set.add(i[1]) 
            if i[1] not in tried_vertex:
                remaning_vertex.add(i[1])
edge_list=list(edge_set)
vertex_list=list(vertex_set)
print(vertex_list,edge_list)
print(len(vertex_list))

g=nx.Graph()
g.add_nodes_from(vertex_list)
g.add_edges_from(edge_list)
print('matrix')
for i in vertex_list:
    for j in vertex_list:
        print(nx.shortest_path_length(g,source=i,target=j),end=' ')
    print()

