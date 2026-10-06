import heapq
from RMP import dict_gn, dict_hn
def astar(start, goal):
    pq = [(dict_hn[start], 0, [start])]   # (f, g, path)
    best_g = {}

    while pq:
        f, g, path = heapq.heappop(pq)
        node = path[-1]
        if node == goal:
            return path, g
        if node in best_g and best_g[node] <= g:
            continue
        best_g[node] = g
        for nb, cost in dict_gn[node].items():
            heapq.heappush(pq, (g + cost + dict_hn[nb], g + cost, path + [nb]))

path, cost = astar('Arad', 'Bucharest')
print(' -> '.join(path), cost) 
