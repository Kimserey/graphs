from graphviz import Digraph

g = Digraph(format='png', filename='test-output/linked-list', engine='circo')

g.graph_attr['rankdir'] = 'LR'
g.edges(['12', '23', '34', '45', '52'])
g.render(view=True)  