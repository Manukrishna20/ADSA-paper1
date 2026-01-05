import networkx as nx
import matplotlib.pyplot as plt

g=nx.Graph()
g.add_nodes_from([1,2,3])
g.add_edges_from([(1,2),(1,3)])

pos=nx.spring_layout(g)
nx.draw(g,pos,with_label=True,node_color='skyblue',edge_color='black')
plt.title("Graph1")
plt.show()

