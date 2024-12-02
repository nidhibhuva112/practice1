mylist=[1,2,3,4,5]
print(mylist)

# Indexing and Slicing

mylist=['one','two','three',4,5]
print(mylist)

print(mylist[1])

num=[9,8,7,6,5]
print(num[1:])
print(num[:3])
print(num[:])
print(num[::-1])

#concatenate list
con=['student']
print(['hello']+con)

#reassign list
new_add=con+['new item permanently']
print(new_add)

print(new_add*2)


#list method
list1=[10,20,30]
#list=list1.append('add element!!')
#print(list)

list2=list1.pop(1)
print(list2)

new_list=['a','b','c','d','e']
print (new_list)
print(new_list.reverse())

list3=[6,7,5,3,8,2,9]
abc=list3.sort()
print(abc)

#nesting list
lst1=[1,2,3]
lst2=[4,5,6]
lst3=[7,8,9]

matrix=[lst1,lst2,lst3]
print(matrix)
print(matrix[0])
print(matrix[0][1])

#list comprehensive
col=[row[0] for row in matrix]
print(col)
