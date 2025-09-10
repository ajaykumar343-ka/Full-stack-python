# ---------------------------
# Arithmetic operators
# --------------------------
# exe
a=20
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a//b)
print(a%b)
# ----------------------------
# program  of the functioning of arithematic operators
# ----------------------------
a=float(input("enter value of a:"))
b=float(input("enter valube of b:"))
print("-"*50)
print("\tresults of arithmetic operators")
print("-"*50)
print("\t\tsum({},{})={}".format(a,b,a+b))
print("\t\tsub({},{})={}".format(a,b,a-b))
print("\t\tdiv({},{})={}".format(a,b,a/b))
print("\t\tmul({},{})={}".format(a,b,a*b))
print("\t\tfloor div({},{})={}".format(a,b,a//b))
print("\t\tpower({},{})={}".format(a,b,a**b))
print("\t\tmood div({},{})={}".format(a,b,a%b))
print("_"*50)
# -----------------------------
# programme for the calculation of the square for number
# ------------------------------
o=int(input("enter your number for cal of square root of given number:"))
res=o**0.5
print("square root({},{})".format(o,res))
# -----------------------------
# programme for showing the dispatchinf of currency in form of notes
# ----------------------------
money=int(input("enter how muvh money do you wnat to withdrawn"))
n500=money//500
money=money%500
n100=money//100
money=money%100
n200=money//200
money=money%200
print("number of 500={}".format(n500))
print("number of 200={}".format(n200))
print("number of 100={}".format(n100))

# ---------------------------
# Assignment operators
# ----------------------------
a=20
b=30
c=a+b
print(a,b,c)

a,b=30,40
print(a,b)
a,b,c=89,"ajay",79
print(a,b,c)
sno,sname,marks=10,"Rossum",34.56
print(sno,sname,marks)

a,b=10,30
print(a,b)
a,b=b,a
print(a,b)
# --------------------
# programm for reading two val and swapping them
# --------------------
a,b=input("enter yor value a:"),input("enter your value b:")
print("-"*50)
print("\toriginal val of a=",a)
print("\toriginal val of b=",b)
print("-"*50)
b,a=a,b
print("\toriginal val of a=",a)
print("\toriginal val of a=",a)
# -----------------------
a,b=float(input("enter yor value a:")),float(input("enter your value b:"))
print("-"*50)
print("\toriginal val of a=",a)
print("\toriginal val of b=",b)
print("-"*50)
b,a=a,b
print("\toriginal val of a=",a)
print("\toriginal val of a=",a)
# ----------------------------
#Relational Operators
# ----------------------------
print(80>20)
print(20<10)
print(10==20)
print(10==10)
print(3!=4)
print(3!=3)
print(10>=3)
print(10<=3)
print(10<=4)
"POGULA">"AJAY"
"AJAYKUMAR">"POGULA"
"aTR">"ATC"

# -----------------------------
# Logical operators
# ----------------------------
# i. 'and' Operator
# ii. 'or' Operator
# iii. 'not' Operator

# ---------------------------
#  i. 'and' Operator
# --------------------------
True and False
False and True
False and False
True and True

10>3 and 40>10
10>20 and 20>30
10>5 and 20>30 and 40>30
10>2 and 30>20 and 30>15 and 40>20

100 and 300
300 and 0
0 and 200
100 and 300 and 400
# -------------------
# ii. 'or' Operator
# --------------------
True or False
False or True
False or False
True or True

10>2 or 20>30
20>10 or 30>40 or 50>60
10>20 or 40>50 or 50>40
10>20 or 40>30 or 50>60 or 50>80
# --------------------
# iii. 'not' Operator
# --------------------
not True
not False

10>20 and 30>40
not(10>20 and 30>40)
10>2 or 30>10
not (100 and 200)
not 100 and not 200
not 0 and not 200-200




































