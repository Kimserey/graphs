from graphviz import Digraph

# normal graph
g = Digraph(format='png', filename='test-output/linked-list/list')
g.graph_attr['rankdir'] = 'LR'
g.attr('node', shape='circle')
g.edges(['12', '23', '34', '45', '52'])
g.render()

# mu
g = Digraph(format='png', filename='test-output/linked-list/mu')
g.graph_attr['rankdir'] = 'LR'
g.attr('node', shape='doublecircle', style='filled')
g.node('2')
g.attr('node', shape='circle', style='')
g.edges(['12', '23', '34', '45', '52'])
g.render()

# lambda
g = Digraph(format='png', filename='test-output/linked-list/lambda')
g.graph_attr['rankdir'] = 'LR'
g.attr('node', shape='circle')
g.node('1')
g.attr('node', shape='doublecircle', style='filled')
g.node('2')
g.node('3')
g.node('4')
g.node('5')
g.edges(['12', '23', '34', '45', '52'])
g.render()

# meeting
g = Digraph(format='png', filename='test-output/linked-list/meeting')
g.graph_attr['rankdir'] = 'LR'
g.attr('node', shape='circle')
g.node('1')
g.node('2')
g.node('3')
g.node('4')
g.attr('node', shape='doublecircle', style='filled')
g.node('5')
g.edges(['12', '23', '34', '45', '52'])
g.render()

# v
g = Digraph(format='png', filename='test-output/linked-list/v')
g.graph_attr['rankdir'] = 'LR'
g.attr('node', shape='circle', style='filled')
g.node('1')
g.attr('node', shape='doublecircle', style='filled')
g.node('2')
g.attr('node', shape='circle', style='')
g.node('3')
g.node('4')
g.attr('node', shape='circle', style='filled')
g.node('5')
g.edges(['12', '23', '34', '45', '52'])
g.render()