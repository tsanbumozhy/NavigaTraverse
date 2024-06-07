from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import matplotlib.pyplot as plt
import networkx as nx
import keyboard
from tkinter import *

#v = int(input("Enter the number of places to be visited : "))
v = 5

def findDistance(graph, path):
    sum = 0
    i=0
    while i+1<len(path):
        sum += graph[path[i]][path[i+1]]
        i +=1

    distance.append(sum)

def hamCycle(graph):
    global distance
    global ways

    ways = []
    distance = []

    path = [0]

    visited = [False] * (len(graph))

    visited[0] = True

    FindHamCycle(graph, 1, path, visited)


def FindHamCycle(graph, pos, path, visited):
    if pos == len(graph):

        if graph[path[-1]][path[0]] != 0:

            path.append(0)

            x = []
            for i in range(len(path)):
                x.append(path[i])

            path.pop()

            ways.append(x)
            findDistance(graph, path)
        return

    for x in range(len(graph)):

        if not visited[x]:
            path.append(x)
            visited[x] = True

            FindHamCycle(graph, pos + 1, path, visited)

            visited[x] = False
            path.pop()


def generategraph(graph, place):
    G1 = nx.Graph()
    loc = []
    for i in range(0, v):
        loc.append(chr(65+i))
    G1.add_nodes_from(loc)

    for i in range(0, v):
        for j in range(0, v):
            G1.add_edge(loc[i], loc[j], distance =round(graph[i][j],2))

    pos = nx.circular_layout(G1)
    nx.draw_networkx(G1, pos, node_size=800)
    labels = nx.get_edge_attributes(G1, 'distance')
    nx.draw_networkx_edge_labels(G1, pos, edge_labels=labels)
    plt.savefig('graph.png')

    for i in range(0, v):
        plt.plot('-b',label=loc[i]+' - '+place[i], linestyle = '', fillstyle = 'full')

    plt.legend()
    plt.show()
    return G1

def generatepathgraph(graph, place, spath):
    G = nx.Graph()
    G.add_nodes_from(['A', 'B', 'C', 'D', 'E'])
    G.add_edge('A', 'C', weight=3.08, label=1)
    G.add_edge('C', 'E', weight=1.24, label=2)
    G.add_edge('E', 'B', weight=3.27, label=3)
    G.add_edge('B', 'D', weight=0.73, label=4)
    G.add_edge('D', 'A', weight=5.90, label=5)

    pos = nx.circular_layout(G)
    nx.draw_networkx(G, pos, node_size=700)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.savefig('graph.png')
    plt.show()
    return G

"main"
loc = Nominatim(user_agent="GetLoc")

area = []
getLoc = []
place = []
graph = []
'''
for i in range(0, v):
    getLoc.append(loc.geocode(input("Enter the Location to be visited : ")))
'''
area.append("Peelamedu, Coimbatore")
area.append("TownHall, Coimbatore")
area.append("Gandhipuram, Coimbatore")
area.append("Ukkadam, Coimbatore")
area.append("Sivananda Colony, Coimbatore")
'''
for i in range(0, v):
    getLoc.append(loc.geocode(area[i]))

for i in range(0, v):
    place.append((getLoc[i].latitude, getLoc[i].longitude))

for i in range(0, v):
    x = []
    for j in range(0, v):
        x.append(geodesic(place[i], place[j]).km)
    graph.append(x)

for i in graph:
    print(i)
'''
graph = [[0.0, 5.17808928361883, 3.0829861429310457, 5.901424053778865, 4.1100626481030655],
        [5.17808928361883, 0.0, 2.846505474611704, 0.7377694693236208, 3.2743797215801336],
        [3.0829861429310457, 2.846505474611704, 0.0, 3.426240117468966, 1.2432892025000002],
        [5.901424053778865, 0.7377694693236208, 3.426240117468966, 0.0, 3.6518122949854415],
        [4.1100626481030655, 3.2743797215801336, 1.2432892025000002, 3.6518122949854415, 0.0]]

generategraph(graph, area)


hamCycle(graph)


short_index = distance.index(min(distance))
for i in range(len(ways[short_index])-1):
    print(chr(65+ways[short_index][i]), end=" --> ")
print(chr(65))
print(ways[short_index])
generatepathgraph(graph, area, ways[short_index])

exit()

root = Tk()

root.title("Shortest path")
for i in range(v):
    Label(root, text="Choose Location ").grid(row=4+i, column=0)

drop = []
e = []
var = []

for i in range(v):
    var.append(chr(65+i))
    drop.append(OptionMenu(root, var[i], 'Peelamedu, Coimbatore', 'TownHall, Coimbatore', 'Gandhipuram, Coimbatore', 'Ukkadam, Coimbatore', 'Sivananda Colony, Coimbatore'))

for i in range(v):
    drop[i].grid(row=4+i, column=2)
    var[i] = StringVar()
    var[i].set('Select')
    e.append(Entry(root, textvariable=var[i]))
    e[i].grid(row=4+i, column=1)

b = Button(root, text="FIND", font='bold', width=30, command=getLoc)
b.grid(row=10, column=2)
root.mainloop()
