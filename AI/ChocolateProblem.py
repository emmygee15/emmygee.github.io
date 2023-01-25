import constraint

problem = constraint.Problem()
problem.addVariables('A', range(31))
problem.addVariables('B', range(45))
problem.addVariables('C', range(76))
problem.addVariables('D', range(101))

def weightConstraint(A, B, C, D):
    if (A*100 + B*45 + C*10 + D*25) <= 3000:
        return  True

def volumeConstraint(A, B,C,D):
    if (A*8*2.5*0.5 + B*6*2*0.5 + C*2*2*0.5 + D*3*3*0.5) <= 3000:
        return  True

def valueConstraint(A, B,C,D):
    if (A*8* + B*6.8+ C*4 + D*3) <= 3000:
        return  True

problem.addConstraint(weightConstraint, 'ABCD')
problem.addConstraint(volumeConstraint, 'ABCD')
problem.addConstraint(valueConstraint, 'ABCD')

maximumSweetness = 20
solutions = problem.getSolutions()

for solution in solutions:
    currentSweetness = solution['A'] * 10 + solution['B'] * 8 + solution['C'] * 4.5 + solution['D'] * 3.5
    if currentSweetness > maximumSweetness:
        maximumSweetness = currentSweetness
        bestSolution = solution

print(bestSolution, maximumSweetness)
