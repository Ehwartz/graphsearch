python main.py


output sample: 



-----------------------------------------------------------------------------------------------------------
BFS
['Arad']
['Sibiu', 'Timisoara', 'Zerind']
['Timisoara', 'Zerind', 'Fagaras', 'Oradea', 'Rimnicu Vilcea']
['Zerind', 'Fagaras', 'Oradea', 'Rimnicu Vilcea', 'Lugoj']
['Fagaras', 'Oradea', 'Rimnicu Vilcea', 'Lugoj']
['Fagaras', 'Oradea', 'Rimnicu Vilcea', 'Lugoj', 'Bucharest']

routine:  ['Arad', 'Sibiu', 'Fagaras', 'Bucharest'] 

-----------------------------------------------------------------------------------------------------------
DFS
['Arad']
['Sibiu', 'Timisoara', 'Zerind']
['Sibiu', 'Timisoara', 'Oradea']
['Sibiu', 'Timisoara']
['Sibiu', 'Lugoj']
['Sibiu', 'Mehadia']
['Sibiu', 'Dobreta']
['Sibiu', 'Craiova']
['Sibiu', 'Pitesti', 'Rimnicu Vilcea']
['Sibiu', 'Pitesti']
['Sibiu', 'Bucharest']

routine:  ['Arad', 'Timisoara', 'Lugoj', 'Mehadia', 'Dobreta', 'Craiova', 'Pitesti', 'Bucharest'] 

-----------------------------------------------------------------------------------------------------------
UCS
['Arad']
[0]
['Sibiu', 'Timisoara', 'Zerind']
[140, 118, 75]
['Sibiu', 'Timisoara', 'Oradea']
[140, 118, 146]
['Sibiu', 'Oradea', 'Lugoj']
[140, 146, 229]
['Oradea', 'Lugoj', 'Fagaras', 'Rimnicu Vilcea']
[146, 229, 239, 220]
['Lugoj', 'Fagaras', 'Rimnicu Vilcea']
[229, 239, 220]
['Lugoj', 'Fagaras', 'Craiova', 'Pitesti']
[229, 239, 366, 317]
['Fagaras', 'Craiova', 'Pitesti', 'Mehadia']
[239, 366, 317, 299]
['Fagaras', 'Craiova', 'Pitesti', 'Mehadia', 'Bucharest']
[239, 366, 317, 299, 450]

routine:  ['Arad', 'Sibiu', 'Fagaras', 'Bucharest'] 

-----------------------------------------------------------------------------------------------------------
GBFS
['Arad']
[366]
['Sibiu', 'Timisoara', 'Zerind']
[253, 329, 374]
['Timisoara', 'Zerind', 'Arad', 'Fagaras', 'Oradea', 'Rimnicu Vilcea']
[329, 374, 366, 178, 380, 193]
['Timisoara', 'Zerind', 'Arad', 'Fagaras', 'Oradea', 'Rimnicu Vilcea', 'Bucharest']
[329, 374, 366, 178, 380, 193, 0]
Fagaras
Sibiu
Arad

routine:  ['Arad', 'Sibiu', 'Fagaras', 'Bucharest'] 

-----------------------------------------------------------------------------------------------------------
A* Search
['Arad']
[366]
['Sibiu', 'Timisoara', 'Zerind']
[393, 447, 449]
['Timisoara', 'Zerind', 'Fagaras', 'Oradea', 'Rimnicu Vilcea']
[447, 449, 277, 531, 273]
['Timisoara', 'Zerind', 'Fagaras', 'Oradea', 'Craiova', 'Pitesti']
[447, 449, 277, 531, 306, 195]
['Timisoara', 'Zerind', 'Fagaras', 'Oradea', 'Craiova', 'Pitesti', 'Bucharest']
[447, 449, 277, 531, 306, 195, 101]
['Arad', 'Sibiu', 'Timisoara', 'Zerind', 'Fagaras', 'Oradea', 'Rimnicu Vilcea', 'Craiova', 'Pitesti', 'Bucharest']

routine:  ['Arad', 'Sibiu', 'Rimnicu Vilcea', 'Pitesti', 'Bucharest'] 

-----------------------------------------------------------------------------------------------------------

Process finished with exit code 0