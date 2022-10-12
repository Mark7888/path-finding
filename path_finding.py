
def find_path(base_matrix, check_pos, end_pos, barrier_char='x', _route_to_final=[], _start_pos=None):
    """ finds the shortest path from start to end position
    @base_matrix: a list of lists where you want to find the path
    @chech_pos -> (x, y): coordinates, where the path starts
    @end_pos -> (x, y): coordinates, where the path ends
    @barrier_char: string representing the walls of the route in the matrix
    """


    if _start_pos == None:
        _start_pos = check_pos

    base_matrix[check_pos[0]][check_pos[1]] = barrier_char # we don't wanna check this anymore
    _route_to_final.append(check_pos)

    where_can_we_go = []

    if base_matrix[check_pos[0]-1][check_pos[1]] != barrier_char: # up
        where_can_we_go.append( (check_pos[0]-1, check_pos[1]) )
    if base_matrix[check_pos[0]][check_pos[1]+1] != barrier_char: # right
        where_can_we_go.append( (check_pos[0], check_pos[1]+1) )
    if base_matrix[check_pos[0]+1][check_pos[1]] != barrier_char: # down
        where_can_we_go.append( (check_pos[0]+1, check_pos[1]) )
    if base_matrix[check_pos[0]][check_pos[1]-1] != barrier_char: # left
        where_can_we_go.append( (check_pos[0], check_pos[1]-1) )
    
    return_routes = []

    for p in where_can_we_go:
        if p == _start_pos:
            continue
        elif p == end_pos:
            return_routes.append(_route_to_final)
        else:
            base_matrix, rtf = find_path(base_matrix, p, end_pos, _route_to_final=_route_to_final.copy(), _start_pos=_start_pos)
            if rtf != None:
                rtf.append(end_pos)
                return_routes.append(rtf)
    
    if len(return_routes) == 0:
        return base_matrix, None
    
    return_routes.sort(key=len) # sort by size

    return base_matrix, return_routes[0]
