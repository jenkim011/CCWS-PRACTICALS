from RMP import dict_gn, dict_hn

start, goal = "Arad", "Bucharest"

def a_star_recursive(curr, g, path):
    if curr == goal:
        print("The A* path is:\n" + " -> ".join(path + [curr]))
        print(f"Total distance: {g} km")
        return True

    # get neighbours sorted by f = g + h
    neighbours = sorted(dict_gn[curr].items(), key=lambda x: g + x[1] + dict_hn[x[0]])

    for nxt, dist in neighbours:
        if nxt not in path:
            if a_star_recursive(nxt, g + dist, path + [curr]):
                return True
    return False

a_star_recursive(start, 0, [])
