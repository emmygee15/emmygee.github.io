import constraint

problem = constraint.Problem()
problem.addVariable("WA", ['Red', 'Green', 'Blue'])
problem.addVariable("NT", ['Red', 'Green', 'Blue'])
problem.addVariable("SA", ['Red', 'Green', 'Blue'])
problem.addVariable("QL", ['Red', 'Green', 'Blue'])
problem.addVariable("NSW", ['Red', 'Green', 'Blue'])
problem.addVariable("VI", ['Red', 'Green', 'Blue'])
problem.addVariable("TA", ['Red', 'Green', 'Blue'])

def myConstraint(wa, nt, sa, ql, nsw, vi, ta):
    if(wa != nt) and (wa != sa) and (sa != nt) and (ql != nt) and (ql != sa) and (ql != nsw) and (nsw != sa) and (nsw != vi) and (vi != sa) and (vi != ta):
        return True

problem.addConstraint(myConstraint, ["WA", "NT", "SA", "QL", "NSW", "VI", "TA"])
solutions = problem.getSolutions()
for solution in solutions:
    print(solution)