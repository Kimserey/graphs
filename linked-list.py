from graphviz import Digraph

g = Digraph(format='png')
g.graph_attr['rankdir'] = 'LR'
g.edges(['12', '23', '34', '45', '52'])
g.render('test-output/linked-list', view=True)  