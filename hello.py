# hello.py - http://www.graphviz.org/content/hello

from graphviz import Source

g = Source("digraph G {\n\tnode0 [label=\"1\"];\n\tnode1 [label=\"2\"];\n\tnode2 [label=\"3\"];\n\tnode3 [label=\"4\"];\n\tnode4 [label=\"5\"];\n\tsubgraph U {\n\t\tedge [dir=none];\n\t}\n\tsubgraph D {\n\t\tnode0 -> node1;\n\t\tnode1 -> node2;\n\t\tnode2 -> node3;\n\t\tnode3 -> node4;\n\t\tnode4 -> node2;\n\t}\n}\n")
g.view()