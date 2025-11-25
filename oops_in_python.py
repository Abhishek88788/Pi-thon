a = (3,4,5,23,3)

b = {3,4,5,23,3}

c = [3,4,5,23,3]

d = {'a':3,'b':4,'c':5,'d':23,'e':3}

e = "345233"

f = 345233

g = 34.5233

h = True

i = None

j = b'345233'

k = 324+6j

l = frozenset({3,4,5,23,3})

m = bytearray(b'345233')

n = range(5)

o = memoryview(b'345233')

p = complex(324,6)

q = float(34.5233)

r = int(345233)

s = str("345233")

t = list([3,4,5,23,3])

u = tuple((3,4,5,23,3))

v = set({3,4,5,23,3})

w = bool(True)

x = dict(a=3,b=4,c=5,d=23,e=3)




for var in [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x]:
    print(type(var))

