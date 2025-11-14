#ASSIGNMENT 1 --  STUDENT NUMBER: 22424217

#imports
import networkx as nx
import matplotlib.pyplot as plt

# create directed graph
G = nx.DiGraph()

# Professor
prof = "Prof. Ansah"

# 15 students 
students = [
    "Bernard", "Ama", "Kojo", "Daniel", "Sarah",    
    "Michael", "Janet", "Yaw", "Kofi", "Akosua",    
    "Kwame", "Doris", "Esther", "Nana", "Felix"     
]

# Create groups of 5 for reasearch
social_network = students[0:5]
machine_learning = students[5:10]
data_visualization = students[10:15]

# Add nodes
G.add_node(prof)
G.add_nodes_from(students)

# Professor supervises each student
G.add_edges_from([(prof, s) for s in students])

# Simple collaboration inside each group
def connect_group(group):
    for i in range(len(group)-1):
        G.add_edge(group[i], group[i+1])

connect_group(social_network)
connect_group(machine_learning)
connect_group(data_visualization)

color_map = []

for node in G.nodes():
    if node == prof:
        color_map.append("yellow")         #Prof Ansah
    elif node in social_network:
        color_map.append("lightgreen")     #Social Network Group
    elif node in machine_learning:
        color_map.append("lightblue")      #Machine Learning Group
    elif node in data_visualization:
        color_map.append("red")            #Data Visulization Group

plt.figure(figsize=(10, 8))

nx.draw(
    G,
    node_color=color_map,
    node_size=1400,
    arrows=True,
    font_size=10,
    font_color="black",
    with_labels=True,
    arrowstyle="-|>",
    arrowsize=15
)

plt.title("Data Science Research Group Network", fontsize=14)
plt.axis("off")
plt.show()


# Calculations for Nodes, Edges and Isolated nodes
print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())

# Degree distribution
degrees = dict(G.degree())
print("\nDegree distribution:")
for node, deg in degrees.items():
    print(f"{node}: {deg}")

# Isolated nodes (nodes with degree = 0)
isolated = list(nx.isolates(G))
print("\nIsolated nodes:", isolated if isolated else "None")