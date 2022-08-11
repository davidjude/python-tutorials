#slicing
name="my name is uba"
print(name[0:10])
print(len(name))
print(name.upper())
print(name.lower())

modified=name.replace("n","t")
print(modified)
#list method

names=["mango","pear","orange","guava","pineapple"]
print(names[0:3])
print(len(names))
names[2]=["uba"]
print(names)


#insert
a=names.insert(1,"dave")
print(names)


#joining list
names2=["dave","obi","chibuike","okeke"]
names.extend(names2)
print(names)

#remove
places=["market","church","school","hospital","mall"]
places.remove("market")
print(places)

#pop
places.pop(1)
print(places)

#tuples method
students={"name":"uba","age":"10","dept":"chemistry"}
print(students["age"])
students.update({"age":"30"})
print(students)
