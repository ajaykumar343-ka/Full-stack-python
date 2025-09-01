# dict

dl={100:"ajju",90:"pawan",44:"rakee",89:"karthik"}
print(dl,type(dl))
len(dl)

d2={"Python":1,"C":2,"Java":3,"C++":4}
print(d2,type(d2))

len(d2)
d3={100:1.2,200:1.3,300:1.2,400:1.3}
print(d3,type(d3))

d1={10:"Apple",20:"Mango",30:"Kiwi",40:"Sberry"}
print(d1,type(d1))
d1[10]
d1[20]
d1[30]
d1[40]

d1={}
print(d1,type(d1),id(d1))
len(d1)
d1[100]=93.4
d1[200]=94.5
d1[300]=95.6
d1[400]=96.7
print(d1,type(d1),id(d1))
# ====================================
# pre defined functionsof dict
# ====================================

# clear()

d1={10:1.2,20:2.2,30:2.3,40:4.4}
print(d1,type(d1),id(d1))
len(d1)
d1.clear()
print(d1,type(d1),id(d1))
len(d1)
print(d1.clear())

# pop()

d1={10:1.2,20:2.2,30:2.3,40:4.4}
print(d1,type(d1),id(d1))
len(d1)
print(d1.pop(10))
print(d1,type(d1),id(d1))
len(d1)
print(d1.pop(20))
print(d1,type(d1),id(d1))
len(d1)
print(d1.pop(30))
print(d1,type(d1),id(d1))

# popitem()

d1={10:1.2,20:2.2,30:2.3,40:4.4}
print(d1,type(d1),id(d1))
print(d1.popitem())
print(d1,type(d1),id(d1))
print(d1.popitem())
print(d1,type(d1),id(d1))

# copy()

d1={10:1.2,20:2.2,30:2.3,40:4.4}
print(d1,type(d1),id(d1))
d2=d1.copy()
print(d2,type(d2),id(d2))

# get ()

xu={9:"ajay",0:"kumar",10:1.2,20:2.2,30:2.3,40:4.4}
print(xu,type(xu),id(xu))

print(xu.get(0))
print(xu.get(20))
print(xu.get(30))
print(xu.get(40))

statescaps={"TS":"HYD","AP":"VIJ","KAR":"BANG","MH":"MUM"}
print(statescaps,type(statescaps))

xlv=statescaps.get("ts")
print(xlv)

xlv=statescaps.get("BAN")
print(xlv)

# keys()

statescaps={"TS":"HYD","AP":"VIJ","KAR":"BANG","MH":"MUM"}
print(statescaps,type(statescaps))

wagnr=statescaps.keys()
print(wagnr)

# values()

statescaps={"TS":"HYD","AP":"VIJ","KAR":"BANG","MH":"MUM"}
print(statescaps,type(statescaps))

wagnr=statescaps.values()
print(wagnr)

#  item()

d1={10:1.2,20:2.2,30:2.3,40:4.4}
print(d1)
kvs=d1.items()
print(kvs,type(kvs))
for kv in kvs:
    print(kv)
    (10, 1.2)
    (20, 2.2)
    (30, 2.3)
    (40, 4.4)













