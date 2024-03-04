print('*** Tests Route ***')
print('La solution devrait s\'afficher:')
curr_rsol = rsol.Route(solvedProblem=frp_inst)
curr_rsol.visit_sequence = [0, 2, 3]
3
print(str(curr_rsol))