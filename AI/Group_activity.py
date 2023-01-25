
import constraint

problem = constraint.Problem()

problem.addVariable("V1",["AI","DB","MATHS","PHY"])
problem.addVariable("V2",["AI","DB","MATHS","PHY"])
problem.addVariable("V3",["AI","DB","MATHS","PHY"])
problem.addVariable("V4",["AI","DB","MATHS","PHY"])
problem.addVariable("V5",["AI","DB","MATHS","PHY"])
problem.addVariable("V6",["AI","DB","MATHS","PHY"])

def myConstraint(V1,V2,V3,V4,V5,V6):
    if(V1!=V2) and (V1!=V4) and (V1!=V5) and (V2!=V3) and (V2!=V5) and (V2!=V4) and (V2!=V6) and (V3!= V5) and (V3!=V6) and (V4!=V5) and (V5!=V6) and (V3!=V5):
        return True

def myConstraint1(V1,V2,V3,V4,V5,V6):
    seats = [V1,V2,V3,V4,V5,V6]
    count = 0
    co = 0
    for i in range(0,len(seats)):
        if(seats[i]=="AI"):
            count = count + 1
            if (count<3) and (count > 1):
                return True
                
        i+=1
    

problem.addConstraint(myConstraint,["V1","V2","V3","V4","V5","V6"]) 
problem.addConstraint(myConstraint1,["V1","V2","V3","V4","V5","V6"])

solutions = problem.getSolutions()

for i in solutions:
    print(i)