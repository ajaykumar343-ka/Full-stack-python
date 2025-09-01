# =========================================
# set()
# =========================================

s1={10,20,30,40,10,20,30,50,60,70}
print(s1,type(s1))
s2={100,"Rossum",45.67,True,2+3j}
print(s2,type(s2))

s=set()
print(s,len(s))

s1={10,20,30,40,50,-10,-20}
print(s1,type(s1))
len(s1)

s="mississippi"
s=set(s)
print(s,len(s))

s2=set(s)
print(s2,len(s2),type(s2))

lst=[10,20,30,10,20,30,40,50,10,20]
print(lst,type(lst))
len(lst)
s1=set(lst)
print(s1,type(s1))

y=200
print(y,type(y))
f=set([y])
print(f,type(f))

k=87.55
print(k,type(k))
l=set([k])
print(l,type(l))
# -------------------------------
# pre  defined functions of set
# -------------------------------

# add ()

o={"python",34,66.45,"men"}
print(o,type(o))
o.add("rossum")
print(o,type(o))

o={"python",34,66.45,"men"}
print(o,type(o))
o.add(0)
print(o)

o.add(True)
print(o)
o.add(100)
print(o)

# remove()

s1={10,"Travis",34.56,True,2+3j}
print(s1,type(s1),id(s1))
s1.remove(10)
print(s1,type(s1),id(s1))
s1.remove(34.56)
print(s1,type(s1),id(s1))
s1.remove(2+3j)
print(s1,type(s1),id(s1))

# discard()

o={"python",34,66.45,"men"}
print(o,id(o),type(o))
o.discard("python")
print(o)

o.discard(34)
print(o)

o.discard(66.45)
print(o)
o.discard("men")
print(o)

# pop()

o={"python",34,66.45,10,"Travis",34.56,True,2+3j,"men"}
print(o,type(o),id(o))
o.pop()
print(o,type(o))
o.pop()
print(o,type(o))
o.pop()
print(o,type(o))
o.pop()
print(o,type(o))
o.pop()
print(o,type(o))

# clear()

o={"python",34,66.45,10,"Travis",34.56,True,2+3j,"men"}
print(o,type(o),id(o))
len(o)
print(o)

o.clear(o)
len(o)
print(o)

# isdisjoint()

s1={10,20,30,40}
s2={30,25,35,45}
s3={55,65,75}

s1.isdisjoint(s2)
s2.isdisjoint(s1)
s3.isdisjoint(s1)
s3.isdisjoint(s2)

y="kumar"
set(y).isdisjoint(set("aeiou"))

set().isdisjoint(set())

# issuperset()

s1={10,20,30,40}
s2={10,20}
s3={15,25,35,10}

s1.issuperset(s2)
s2.issuperset(s1)

set().issuperset(set())

# issubset()

s1={10,20,30,40}
s2={10,20}
s3={15,25,35,10}

s2.issubset(s1)
s3.issubset(s1)
s1.issubset(s2)
set().issubset(set())
set().issubset({10,20,30})

# union()

s1={10,20,30}
s2={30,40,50}
print(s1,type(s1))
print(s2,type(s2))

s3=s1.union(s2)
print(s3,type(s3))

s4=s1.union(s2,{"a","e","i","o","u"})
print(s4,type(s4))
  
# intersection

s1={30,40,50}
s2={10,20,30,40}
print(s1,type(s1))
print(s2,type(s2))

s3=s1.intersection(s2)
print(s3,type(s3))

s4=s3.intersection(s1)
print(s4,type(s4))

set("RADAR").intersection(set("NISSON"))

# difference()

s={88,34,40,55,40,20,20,23}
s1={10,20,30,40,50}
s2=s.difference(s1)
print(s2,type(s2))

set("AJAYKUMAR").difference(set("RADAR"))

# symmetric_difference()

s={10,20,30,40,50}
s1={20,30,60,70,80}
s2=s.symmetric_difference(s1)
print(s2,type(s2))

set("radar").symmetric_difference(set("nissor"))

set("RADAR").symmetric_difference(set("RADAR"))

# update()

s1={10,20,30}
s2={40,50,60}
print(s1,id(s1))
print(s2,type(s2))

s1.update(s2)
print(s1,type(s1),id(s1))

s2.update(s1)
print(s2,type(s2),id(s2))

s1={10,20,30}
s2={15,25,35}
s3=s2.update(s1)
print(s2)

# copy()
s1={10,20,30}
print(s1,id(s1))
s2=s1.copy()
print(s2,id(s2))

s1.add(100)
s2.add("PY")
print(s1,id(s1))
print(s2,id(s2))

# symmetric_difference_update()

s1={10,20,30}
s2={20,30,40}
s1.symmetric_difference_update(s2)
print(s1)

s1={10,20,30}
s2={20,30,10}
s1.symmetric_difference_update(s2)
print(s1)

s1={10,20,30}
s1.symmetric_difference_update({15,25})
print(s1)


