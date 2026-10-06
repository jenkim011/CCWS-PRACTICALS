import queue as Q
from RMP import dict_gn
start = 'Arad'
goal = 'Bucharest'
def BFS():
    queue = Q.Queue()
    visited = []
    queue.put(start)
    print("BFS traversal from", start, "to", goal, "is:")
    while not queue.empty():
        city = queue.get()
        if city not in visited:
            visited.append(city)
            print(city, end=" ")
            if city == goal:
                break
            for next_city in dict_gn[city]:
                if next_city not in visited:
                    queue.put(next_city)
BFS()
