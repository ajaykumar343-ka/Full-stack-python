# =================
# nested list
# =================
lst=[10,'Rossum',[30,35,25],[70,65,60],'JNTU']
print(lst,type(lst),id(lst))
for val in lst:
    print(val,"--->",type(val),"-->",id(lst))
lst[2].append(87)
lst[-2].insert(0,"good")

print(lst)

lst[-2][::3]
print(lst)

lst[2]+lst[3]
print(lst)

lst=[10,'Rossum',[30,35,25,38],[70,58,65,60],[35,38,58,60],'JNTU']
print(lst)
lst[2][1]=lst[-2][1]+lst[-2][1]
print(lst)
lst[-2][-1:]

[10, 'Rossum', [30, 35, 25, 38], [70, 58, 65, 60], 'JNTU']
del lst[2:4]
print(lst)

lst.insert(-1,[10,30,50])
print(lst)

lst=[100,"RS",[18,19,17],[67,80,76], "JNTU"]
print(lst,type(lst))
for val in lst:
    print(val,"-->",type(val),"--->",type(lst))

lst=[[10,20,30],[40,50,60],[70,80,90]]
print(lst)
for i in lst:
    print(i)
print(lst)

# ============================================================
# tuple
# ============================================================

t1=(10,"Rossum",(17,16,18),(77,78,66),"OUCET")
print(t1,type(t1))
t1[1]
t1[3]
t1[4]
t1[-2][2]

t1=(10,"Rossum",[17,16,18],[77,78,66],"OUCET")
print(t1,type(t1))
t1[2].sort()

t1=()
print(t1,type(t1))

t2=tuple()
print(t2,type(t2))
len(t2)
t2=(100,"RS",34.56,True,2+3j)
print(t2,type(t2))

len(t2)

t3=10,"Travis",45.67,"HYD"
print(t3,type(t3))
s="PYTHON"
print(s,type(s))
t=tuple(s)
print(t,type(t))

s="python"
print(s,type(s))
t=tuple([s])
print(t,type(t))

a=10
print(a,type(a))
t=tuple(a,)
print(t,type(t))
# =====================
# Function in tuple
# =====================
# 1)index()
# 2) count()

# index():-------

t1=(10,"RS",45.67)
print(t1,type(t1))
t1.index(10)
t1.index("RS")
t1.index(45.67)

t1=(10,20,30,40,50,10)
print(t1,type(t1))
t1.index(40)
t1.index(10,)

# 2) count():----
t1=(10,20,30,40,50,10)
print(t1,id(t1),type(t1))
t1.count(10)
t1.count(20)
t1.count(30)
t1.count(40)
t1.count(50)


t2=t1
print(t2,type(t2),id(t2))

t1=(10,-34,0,10,23,56,76,21)
print(t1,type(t1))
t1.sort()
x=sorted(t1)
print(x,type(x))
t1=tuple(x)
print(t1,type(t1))
t2=t1[::-1]





