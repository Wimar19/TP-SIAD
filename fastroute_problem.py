
import problem as prob

class FastRouteProb(prob.Problem):
    def __init__(self):
        super().__init__()
        print('FastRoute::init')


import copy

class FastRouteProb(prob.Problem):
    def __init__(self, dist_matrix=[[]]):
        super(FastRouteProb, self).__init__()
        self._dist_matrix = copy.deepcopy(dist_matrix)
    def __str__(self):
        tmp_str = ''
        for a_list in self._dist_matrix:
            tmp_str = tmp_str + ', '.join([str(i) for i in a_list])
            tmp_str = tmp_str + '\n'
        return str(tmp_str)