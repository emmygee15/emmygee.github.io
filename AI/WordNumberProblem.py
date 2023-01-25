import constraint

problem = constraint.Problem()

problem.addVariables("TF", range(1, 10))  
problem.addVariables("WOUR", range(10))


def sum_constraint(t, w, o, f, u, r):  
    if 2*(t*100 + w*10 + o) == f*1000 + o*100 + u*10 + r:
        return True


problem.addConstraint(sum_constraint, "TWOFUR")


problem.addConstraint(constraint.AllDifferentConstraint())

solutions = problem.getSolutions()  

for solution in solutions:  
    print(solution)
