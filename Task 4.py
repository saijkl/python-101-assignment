list1=[2.13,24,67,45,78]
list2=[4,23,34,56,89,101]
list3=list1+list2
print(list3)
list3.sort()
temp=list3[0]
list3[0]=list3[-1]
list3[-1]=temp
print(list3)