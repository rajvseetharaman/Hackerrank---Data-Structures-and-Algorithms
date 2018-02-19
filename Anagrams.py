def number_needed(a, b):
    a=list(a)
    b=list(b)
    a1=dict()
    b1=dict()
    for x in a:
        if x in a1.keys():
            a1[x]+=1
        else:
            a1[x]=1
            
    for x in b:
        if x in b1.keys():
            b1[x]+=1
        else:
            b1[x]=1
    common=list(set(a1.keys()) & set(b1.keys()))
    sum=0
    for i in common:
        sum+=min(a1[i],b1[i])
    return(len(a)+len(b)-2*sum)

    

a = input().strip()
b = input().strip()

print(number_needed(a, b))
