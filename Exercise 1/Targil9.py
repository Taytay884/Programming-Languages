a=1
class A:
 global a
 print("class A : ",a)
 a = 2
 def __init__(self):
    self.a = 2
    print("class A:: init ", a)
 def thefunc(self):
    a = 3
    print("class A:: thefunc ",a)
class B(A):
    A.a = 4
    def __init__(self):
        self.a = 28
class C(B):
# 2
####################### No Additional Code needed
 print(a)
 def __init__(self):
    j=super()
    print(j.a)
    p=A()
    print(p.a)
 def thefunc(self):
    print(B.a)
class D(C,B):
 a = 4
 def __init__(self):
    global a
# 3
####################### No Additional Code needed
a=7
a1 = A()
b = B()
c = C()
d = D()
a1.thefunc()
b.thefunc()
d.thefunc()