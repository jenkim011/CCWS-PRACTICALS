from RMP import dict_gn
start = 'Arad'
goal = 'Bucharest'
def DFS():
    stack = [start]
    visited = []
    print("DFS traversal from", start, "to", goal, "is:")
    while stack:
        city = stack.pop()
        if city not in visited:
            visited.append(city)
            print(city, end=" ")
            if city == goal:
                break
            for next_city in dict_gn[city]:
                if next_city not in visited:
                    stack.append(next_city)
DFS()
