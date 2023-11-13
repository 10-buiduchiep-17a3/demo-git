#8.1
print("Bài toán tìm số lớn nhất và nhỏ nhất.")
a=eval(input("Nhập số a:"))
b=eval(input("Nhập số b:"))
c=eval(input("Nhập số c:"))
d=eval(input("Nhập số d:"))
g=0
h=0
while(g<a)or(g<b)or(g<c)or(g<d):
    g+=1
h=g
while(h>a)or(h>b)or(h>c)or(h>c):
    h-=1
print("max =",g)
print("min =",h)

#8.2
a=eval(input("Nhập số:"))
print("Giá trị tuyệt đối của",a,"là:","|",a,"|=",abs(a))

#8.3
print("Giải phương trình ax+b=0")
a = int(input("Nhập số a:"))
b = int(input("Nhập số b:"))
if a == 0:
    if b == 0:
        print("Phương trình vô số nghiệm.")
    else: print("Phương trình vô nghiệm.") 
else: 
    print('Nghiệm của phương trình là: x = ', -b/a)

#8.4
a = eval(input("nhap do dai canh a: "))
b = eval(input("nhap do dai canh b: "))
c = eval(input("nhap do dai canh c: "))
if a+b<c and b+c<b:
    print("day khong phai la tam giac")
else:
    print("day la mot tam giac")
    import math
    p=(a+b+c)/2
    S= math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("Dien tich tam giac tren la: ",S)


#8.5
a = int(input("Nhập năm: "))
if ((a%4==0) and (a%100!=0) or (a%400==0)):
    print("năm", a, "là năm nhuận")
else:
    print("năm", a, "không phải là năm nhuận")

#8.9
a = int(input("nhap so a: "))
for i in range(a,0,-1):
    print(i)

#8.10
print("Nhập n:")
n=eval(input(""))
print("Nhập x:")
x=eval(input(""))
s=(x*x+1)**n
print("(S=x*x+1)^n =",s)

#8.11
print("Nhập n:")
n=eval(input(""))
print("Nhập x:")
x=eval(input(""))
A=(x*x+x+1)**n + (x*x-x+1)**n
print("A=(x*x+x+1)^n+(x*x-x+1)^n=",A)