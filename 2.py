list1=["apple","banana","cherry","orange"]
print(list1)
print(type(list1))
for x in list1:
    print(x)

print()

list1[2]="watermelone"
print(list1)

print(len(list1))

print(list1.pop())
print(list1)
list1.insert(1,"Strawberry")
print(list1)

print()

tuple1=("car","van","bike")
print(tuple1)
print(type(tuple1))
list1.extend(tuple1)
print(list1)

print()

set1={'a','b','c','d',}
print(set1)
print(type(set1))

print()

set2={'a','b','c','d','a'}
print(set2)
set2.add('e')
print(set2)

di1={"number": 2,"brand":"Sofa"}
print(di1)
print(type(di1))
