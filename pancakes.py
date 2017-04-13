import heapq

# desde el estado inicial (lista de falses y trues) llegar a un estado de todo trues
# la unica operación permitida es flip(n), en el que se cambia el estado de las posiciones
# n a n+size - 1 de la lista

def flip(s, p, k):
    return [not b if p <= a < p + k else b for a,b in enumerate(s)]


def pancakes(initial_state, k):
    n = len(initial_state)

    frontier = [(0, initial_state)] # a priority queue
    explored = []

    while True:
        if frontier == []:
            return None

        (cost, current) = frontier[0]
        heapq.heappop(frontier)
        #print (cost, current)
        if all(current):
            return cost

        if current not in explored:
            explored.append(current)
            for i in range(n - k + 1):
                neighbor = flip(current, i, k)
                if neighbor not in explored:
                    heapq.heappush(frontier, (cost + 1, neighbor))

if __name__ == '__main__':
    initial = [False, False, False, True, False, True, True, True]
    size = 3
    print (pancakes(initial, size))
    
