list1 = [int(i) for i in input("Enter the list of numbers:").split()]
new_list=[]
[new_list.append(j) for j in list1 if j>0]
print(new_list)
