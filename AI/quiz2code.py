import constraint

myproblem = constraint.Problem()

#S,M,T cannot be zero - so range 1-10
myproblem.addVariables("SMT", range(1, 10))  
# print(myproblem)

#Others (ENDHYO) can be any value upto 10 - value cannot be repeated
myproblem.addVariables("ENDHYO", range(10))


#Defining custom constraint
def sum_constraint(s,e,n,d,m,t,h,y,o):  
    #send + me + the == money
    if (1000*s + 100*e + 10*n + d) + (10*m + e) + (100*t + 10*h + e) == (10000*m + 1000*o + 100*n + 10*e + y):
       return True

#Add custom constraint
myproblem.addConstraint(sum_constraint, "SENDMTHYO")

#Inbuilt constraint to ensure all values are different
myproblem.addConstraint(constraint.AllDifferentConstraint())
print(myproblem.getSolutions())
#Store solutions
solutions = myproblem.getSolutions()  
print(solutions)

#display solutions
for solution in solutions:  
    print(solution)

