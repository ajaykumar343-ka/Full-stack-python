# ==================================================================
# # 1.string
# ==================================================================
s="ajaykumar,good boy"
print(s)

d='''h:no-18-14/1
gurmurty nagar,
idpl colony,
balanagr,hyderabad,
pin code:500037'''

print(d)

h="invented,by the,dudio van rossum"
print(h)

n="@#$%^&_"
print(n)

m="652352469"
print(m)

k='a'
print(k)

addr2='''Travis Oliphant
HNO:12-34, Sea Side
Numpy Organization
Nether lands-58'''

print(addr2)
f="""python programming"""
print(f)

f="python programming"
print(f)

# =====================================================================================
# operations on the string datatype

# indexing operation and slicing operation
# --------------------------------------
# indexing operation:----
# --------------------------------------

g="AJAYKUMAR"
print(g)

g [2]
g [5]

s="PYTHON"
print(s)
s[4]
s[-2]
s[4]
s[-3]

"PYTHON"[0xF-0xA]

"PYTHON"[True]
"PYTHON"[-True]
"PYTHON"[False]

"AJAYKUMAR"[len("PYTHON")]
# -------------------------------------
# slicing operation
# -------------------------------------
M="AJAYKUMAR"
M[2:5]
M[1:4]
M[4:6]
M[-1:1]
M[1:-1]
M[-4:6]
M[-3:2]
M[2:-1]
M[2:1000]
M[-2000:-1]
M[-9:0]
M[-9:-1]
M[0:-7]
M[0:10]
M[True:-True]

M[False:-True]
# =========================================================================

# TYPE CASTING TECHNIQUES
# --------------------
# INT():-
# ---------------------
# float type into int type--(possible)

y=34.56
print(y,type(y))
j=int(y)
print(j,type(j))

n=78.9
print(n,type(n))
h=int(n)
print(h,type(h))

#bool type to into type--(possible)

a=True
print(a,type(a))
x=int(a)
print(x,type(x))

x=False
print(x,type(x))
c=int(x)
print(c,type(c))

# COMPLEX type into int type--(not possible)

c=3+4j
print(c,type(c))
d=int(c)
print(d,type(d))

# ----------------------------
#2. FLOAT()
# ----------------------------

# int type into float type--Possible
A = 10
print(A, type(A))
B = float(A)
print(B, type(B))

C = 120
print(C, type(C))
D = float(C)
print(D, type(D))

# bool type into float type--Possible

E = True
print(E, type(E))
F = float(E)
print(F, type(F))

X=False
print(X,type(X))
C=float(X)
print(C,type(C))

# complex type into float type---Not Possible
G = 3 + 4j
print(G, type(G))
b=float(G)
# --------------------
# 3.BOOL()
# --------------------
# int type into bool type--Possible
j=30
print(j,type(j))
k=bool(j)
print(k,type(k))

d=3434
print(d,type(d))
l=bool(d)
print(l,type(l))

# float type into bool type--Possible
m=69.0
print(m,type(m))
n=bool(m)
print(n,type(n))

o=0.0
print(o,type(o))
p=bool(o)
print(p,type(p))

# complex type into bool type--Possible

q=3+4j
print(q,type(q))
r=bool(q)
print(r,type(r))

i=3+8j
print(i,type(i))
h=bool(i)
print(h,type(h))

# -----------------
# 4. complex()
# -----------------
# int type into complex type--Possible

a=10
print(a,type(a))
b=complex(a)
print(b,type(b))

c=20
print(c,type(c))
d=complex(c)
print(d,type(d))

# float type into complex type--Possible
e=30.5
print(e,type(e))
f=complex(e)
print(f,type(f))

g=40.8
print(g,type(g))
h=complex(g)
print(h,type(h))

# bool type into complex type--Possible
i=True
print(i,type(i))
j=complex(i)
print(j,type(j))

k=False
print(k,type(k))
l=complex(k)
print(l,type(l))
# ===============================================================================
# 2. bytes
# ===============================================================================
lst=[145,178,199,0,134,255,156]
print(lst)
b=bytes(lst)
print(b,type(b))

lst=[145,178,199,0,134,255,156]
print(lst,type(lst))
b=bytes(lst)
print(b,type(b))

lst=[145,178,199,0,134,255,156]
print(lst,type(lst))
b=bytes(lst)
print(b,type(b))
b[0]
b[-5]
b[4]
# ===============================================================================
# bytearray
# ===============================================================================

lst=[195,188,99,0,114,245,156]
print(lst,type(lst))
b=bytearray(lst)
print(b,type(b))

for value in b:
    print(value)
    195
    188
    99
    0
    114
    245
    156
print(b,type(b),id(b))

for val in b[::2]:
    print(val)
    195
    99
    114
    156
    199
for val in b[::1]:
    print(val)
    195
    188
    99
    0
    114
    245
    156
# ===============================================================================
# range
# ===============================================================================
r=range(10)
print(r,type(r))

for i in r:
    print(i)
for v in range(20):
    print(v)

for i in range(10,25):
    print(i)

for v in range(100,199):
    print(v)

o=range(20,30,2)
print(o,type(o))

for k in o:
    print(k)
f=range(10,17)
print(f)

for val in range(10,17):
    print(val)

