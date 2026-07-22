from graph import graph

with open("workflow_graph.png", "wb") as f:
    f.write(graph.get_graph().draw_mermaid_png())

print("Workflow graph saved as workflow_graph.png")