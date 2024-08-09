list1=[1,1000]
leng=len(list1)
length=len(list1)//2
remain=len(list1)-length
list1.sort()
print(list1)
list2=list1[remain:leng]
list1=list1[:remain]

print(list2)
print(list1)
list3=[]
j=0
k=0

for i in range(leng):
    if i%2==0:
       list3.append(list1[j])
       j=j+1
    else:
        list3.append(list2[k])
        k=k+1

print(list3)