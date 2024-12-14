def estEtatFinal(t):
    return t == [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

def transitions(t):
    neighbors = []
    x, y = position_case_vide(t)
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dx, dy in moves:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_t = [row[:] for row in t]
            new_t[x][y], new_t[new_x][new_y] = new_t[new_x][new_y], new_t[x][y]
            neighbors.append(new_t)
    return neighbors

def position_case_vide(t):
    for i in range(3):
        for j in range(3):
            if t[i][j] == 0:
                return i, j
    return -1, -1

def recherche_DFS(etat_depart, goal, L):
    freeNodes = [(etat_depart, [etat_depart])]
    closedNodes = []
    success = False
    explored_states = 0  

    while freeNodes and not success:
        firstNode, path = freeNodes.pop()
        closedNodes.append(firstNode)

        generatedStates = transitions(firstNode)
        new_generated_states = []

        for s in generatedStates :
            if s not in closedNodes :
                new_path = path[:] 
                new_path.append(s)
                new_generated_states.append((s , new_path))

        for s, s_path in new_generated_states:  
            if estEtatFinal(s):
                success = True
                return s_path
            if len(s_path) <= L:
                freeNodes.append((s, s_path))
                closedNodes.append(s)
    return []

t = [[1, 2, 3],
     [8, 6, 0],
     [7, 5, 4]] 
goal = [[1, 2, 3],
        [8, 0, 4],
        [7, 6, 5]]
  
L = 3
ans = recherche_DFS(t , goal, L) 


if(ans == []) :
    print("No answer in depth L")
else :
    for mat in ans :
        for row in mat:
            for x in row : 
                print(x , " " , end="")
            print()
        print()

