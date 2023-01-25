#from kanren import *
#from kanren.constraints import neq, isinstanceo

#x, y = var(), var()

# print(run(0, x, membero(x,(1, 2, 3)), neq(x,3), neq(x,1)))
#print(run(0,x, isinstanceo(x, int), membero(x,(1.1, 1.2, 3))))

from kanren import run, eq, membero, var
from kanren.constraints import neq, isinstanceo
p,q=var(),var()

#Modus ponen
print( run(0, q,    eq(p, q),  membero(p, (True,False)),membero(q, (True,False)), eq(p, True)))

#Modus Tollens
print( run(0, p,    eq(p, q),   membero(p, (True,False)),membero(q, (True,False)), neq(q, True)))

#Hypothetical Syllogism
r=var()
print( run(0, p,  eq(p, q),  eq(q, r),  membero(p, (True,False)),
           membero(q, (True,False)),membero(r, (True,False)), eq(r, True)))

