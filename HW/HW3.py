import numpy as np
from scipy.optimize import linprog

c = [-2, -3] 

A = [[1, 2], [3, 1]]


b = [20, 30]

x_bounds = (0, None)
y_bounds = (0, None)

result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

if result.success:
    print("Optimal value:", -result.fun)  
    print("x values:", result.x)
else:
    print("No solution found.")
