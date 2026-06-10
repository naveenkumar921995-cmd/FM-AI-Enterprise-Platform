from backend.graph import run_graph

query = "AHU compressor tripping continuously"

response = run_graph(query)

print(response)