
import problem as prob
import solution as sol
import solver
import fastroute_problem as frp
import route_solution as rsol

print('Test des constructeurs des classes de base:')
my_prob = prob.Problem()
my_sol = sol.Solution()
my_solver = solver.Solver()

print('\nTest des constructeurs des classes spécialisées:')
my_frp = frp.FastRouteProb()
my_rsol = rsol.Route()

print('\nTest des fonctions d\'une solution:')
my_sol.evaluate()
my_sol.validate()

print('\nTest des fonctions d\'une route:')
my_rsol.evaluate()
my_rsol.validate()
print('\nTest du polymorphisme:')
for sol in (my_sol, my_rsol):
    sol.evaluate()
    sol.validate()


print('*** Tests FrpProblems ***')
print('L\'instance devrait s\'afficher:')
dist_matrix = [[0, 20, 30, 40],
                [20, 0, 30, 5],
                [30, 30, 0, 10],
                [40, 5, 10, 0]]
frp_inst = frp.FastRouteProb(dist_matrix=dist_matrix)
print(str(frp_inst))

print('*** Tests Route ***')
print('La solution devrait s\'afficher:')
curr_rsol = rsol.Route(solvedProblem=frp_inst)
curr_rsol.visit_sequence = [0, 2, 3]
print(str(curr_rsol))
