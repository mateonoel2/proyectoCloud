import pygraphviz as pgv
from IPython.display import Image

# Create a new directed graph
G = pgv.AGraph(directed=True)

# Add nodes
nodes = [
    "Usuario (UI)", 
    "AWS Elastic Beanstalk (Flask)", 
    "AWS EC2 (Machine Learning Model)", 
    "AWS S3 (static files: css, js, images, models)",
    "AWS RDS (Database storage)"
]
for node in nodes:
    G.add_node(node, shape='box')

# Add edges
edges = [
    ("Usuario (UI)", "AWS Elastic Beanstalk (Flask)"), 
    ("AWS Elastic Beanstalk (Flask)", "AWS EC2 (Machine Learning Model)"),
    ("AWS EC2 (Machine Learning Model)", "AWS Elastic Beanstalk (Flask)"),
    ("AWS Elastic Beanstalk (Flask)", "AWS S3 (static files: css, js, images, models)"),
    ("AWS S3 (static files: css, js, images, models)", "AWS RDS (Database storage)")
]
for edge in edges:
    G.add_edge(edge[0], edge[1])

# Write the dot file
G.write('architecture.dot')

# Render the graph to a file (e.g., in PNG format)
G.draw('architecture.png', prog='dot', format='png')

# Display the graph
Image(filename='architecture.png')
