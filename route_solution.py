import solution as sol
class Route(sol.Solution):
    def __init__(self):
        super().__init__()
        print('Route::init')
    self.sequence = []
    self.totalTime = 0

    def evaluate(self):
        print('Route::evaluate')
    def validate(self):
        print('Route::validate')


import solution as sol
import fastroute_problem as frp
import sys
class Route(sol.Solution):
    def __init__(self,solvedProblem=frp.FastRouteProb()):
    super(Route, self).__init__()
    self.visit_sequence = []
    self.problem = solvedProblem
def __str__(self):
    tmp_str = ', '.join([str(i) for i in self.visit_sequence])
    return str(tmp_str)