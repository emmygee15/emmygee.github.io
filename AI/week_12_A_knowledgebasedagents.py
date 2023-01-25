import constraint

problem = constraint.Problem()
problem.addVariables('E', range(1, 100))
problem.addVariables('M', range(1, 20))
problem.addVariables('A', range(1, 10))




def emmanuelcost(E,M,A) :
    if(E*1 + M*5 + A*10) <= 100:
        return True

def emmanuelquantity(E,M,A) :
    if(E + M + A) <= 80:
        return True

problem.addConstraint(emmanuelcost, 'EMA')
problem.addConstraint(emmanuelquantity, 'EMA')

solutions = problem.getSolutions()

for solution in solutions:
    print(solution)