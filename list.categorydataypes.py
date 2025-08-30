# =====================================
# list
# =====================================
lst1=[10,20,3,15,100,2000,-45,10,20]
print(lst1,type(lst1))

lst2=[23,45.5,"hello",3+8j,True,False]
print(lst2,type(lst2))

lst2=[23,45.5,"hello",3+8j,True,False]
lst2[-3]
lst2[2:-2]
lst2[-1]
lst2[0]=1000
print(lst2)

lst1=[]
print(lst1,type(lst1))

lst2=[100,"Rossum",45.67,True,2+3j]
print(lst2)

s="ajaykumar"
print(s,type(s))
lst1=list(s)
print(lst1,type(lst1))

print(lst1,type(lst1),id(lst1))

s="PYTHON"
print(s,type(s))
lst1=list[(s)]
print(lst1,type(lst1),id(lst1))


a=10
print(a,type(a))
lst1=list[a]
print(lst1,type(lst1))


a=2.34
print(a,type(a))
lst1=list[a]
print(lst1,type(lst1),id(lst1))
# -------------------------------------------------------
# Pre-Defined Functions in List
# -------------------------------------------------------

# 1. append()

lst1=[10,20,30]
print(lst1)
lst1.append(40)
print(lst1)

ps4=["ajay",76,345,7,78,3,]
print(ps4,type(ps4),id(ps4))
ps4.append("python")
print(ps4,type(ps4),id(ps4))

# 2. insert()

you=["ajay",89,True,45,87]
print(you,type(you),id(you))
you.insert(2,"python")
print(you,type(you),id(you))

hi=["rossum",834,False,5+7j]
print(hi,type(hi),id(hi))
hi.insert(-1,"man")
print(hi,type(hi),id(hi))

# 3. remove()

lst1=[10,20,30,10,40,20,30,20,10,15]
print(lst1,type(lst1),id(lst1))
lst1.remove(20)
print(lst1,id(lst1))

lst1.remove(30)
print(lst1,id(lst1))

lst1.remove(10)
print(lst1,id(lst1))

# 4. pop(index)

lst1=[10,20,30,10,40,20,30,20,10,15]
print(lst1,type(lst1),id(lst1))
lst1.pop(-1)
print(lst1,type(lst1),id(lst1))

ku=[23,45.5,"hello",3+8j,True,False]
print(ku,type(ku),id(ku))
ku.pop(3)
print(ku,type(ku),id(ku))

# 5. pop()

lst1=["ajay",87,234,45,4+8j,"men"]
print(lst1,type(lst1),id(lst1))
lst1.pop()
print(lst1,type(lst1),id(lst1))

lst=[10,"Rossum",34.56,"Python",2+3j]
print(lst)
lst.pop()
print(lst)

# 6. clear()

lst1=["kumar",87,234,45,4+8j,"boy"]
print(lst1,len(lst1))
lst1.clear()
print(lst1,type(lst1),len(lst1))

#  dell operator

lst=[10,"Rossum",34.56,"Python",2+3j]
print(lst,id(lst))
del lst[-2]
print(lst,id(lst))

del lst[1]
print(lst,id(lst))

# index()

a="MISSISSIPPI"
print(a,type(a))
mp5=list(a)
print(mp5,type(mp5))
mp5.index("M")
mp5.index("I")
mp5.index("S")
mp5.index("P")

# enumerate()

a="MISSISSIPPI"
print(a,type(a))
ak7=list(a)
print(ak7,type(ak7))

for value in enumerate(ak7):
    print(value)

for index,value in enumerate(ak7):
    print(index,"-->",value)

for i,x in enumerate(ak7):
    print(i,"--->",x)

j="ajju","vijju"
print(j)
k=list(j)
print(k,type(k))

for a,v in enumerate(k):
    print(a,"--->",v)

# count()

a="ajjuvijju"
print(a)
lst=list(a)
print(lst,type(lst))


lst.count("j")
lst.count("u")

lst=[10,20,30,10,20,30,40,50,10,20,56]
print(lst)
lst.count(10)
lst.count(20)
lst.count(30)
lst.count(40)
lst.count(50)
lst.count(56)

# copy()

lst1=[19,879,4.4,"rs","python"]
print(lst1)
lst2=lst1.copy()
print(lst2)

lst2.append("new")
lst1.append("True",1)

# reverse()

lst1=["ajay",87,234,45,4+8j,"men"]
print(lst1,id(lst1))
lst2=lst1.reverse()
print(lst1,id(lst1))

# sort()

lst=[10,15,2,3,14,25,-6,0,-3]
print(lst)
lst.sort()
print(lst)

lst.reverse()
print(lst)

lst.sort()
print(lst)

lst=["Rossum","Rajesh","Trump","Anil","Biden"]
print(lst)
lst.sort()
print(lst)

lst.reverse()
print(lst)

lst.sort()
print(lst)

# extend()

lst1=[10,20,30]
print(lst1)
lst2=["rs","ajay","kumar"]
lst1.extend(lst2)
print(lst1)
