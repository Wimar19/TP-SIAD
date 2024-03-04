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
    
    def validate(self):
        locations_list = list(range(0, self.problem.count_locations()))
        if sorted(self.visit_sequence) == locations_list:
            return True
        return False