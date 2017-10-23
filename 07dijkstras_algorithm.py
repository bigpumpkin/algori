
graph = {'start': {'a': 6, 'b': 2},'a':{'fin':1},'b':{'a':3,'fin':5},'fin':{}}
'''graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}'''


infinity = float("inf")
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

processed = []
def find_lowest_cost_node(costs):
	lowest_cost = float("inf")
	lowest_cost_node = None
	for node in costs:
		cost = costs[node]
		if cost < lowest_cost and node not in processed:
			lowest_cost = cost
			lowest_cost_node = node
	return lowest_cost_node


node = find_lowest_cost_node(costs)
while node is not None:
	cost = costs[node]
	neighbors = graph[node]
	for k in neighbors.keys():
		new_cost = cost + neighbors[k]
		if costs[k] > new_cost:
			# ... update the cost for this node.
			costs[k] = new_cost
			# This node becomes the new parent for this neighbor.
			parents[k] = node
	processed.append(node)
	node = find_lowest_cost_node(costs)

print "Cost from the start to each node:"
print costs
