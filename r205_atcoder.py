s=input()
ans=0
k=0
k2=[]
k1=[]
s1=""
i=0
while i<len(s) :
    for j in range(i,len(s)):
        if s1==s[i:j+1]:
            continue
        else:
            s1=s[i:j+1]
            #print(s1)
            ans+=1
            i=j
            break
    i+=1

        
    
if ans==0:
    ans=1


print(ans)