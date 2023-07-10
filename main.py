from pyvis.network import Network

net = Network(notebook=True)

net.add_node(1, color='#000090')

net.add_node(2, color='#200') # node id and label = 2

net.add_edge(1,2,weight=0.87)

net.toggle_physics(True)
net.show('graph.html')

