graph = {}
graph['start'] = {}
graph['start']['a'] = 5
graph['start']['b'] = 0
graph['a'] = {}
graph['a']['c'] = 15
graph['a']['d'] = 20
graph['b'] = {}
graph['b']['c'] = 30
graph['b']['d'] = 25
graph['c'] = {}
graph['c']['fin'] = 20
graph['d'] = {}
graph['d']['fin'] = 10
graph['fin'] = {}
costs = {}

costs['a'] = 5
costs['b'] = 0
costs['c'] = float("inf")
costs['d'] = float("inf")
costs['fin'] = float("inf")
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['c'] = 'start'
parents['d'] = 'start'
parents['fin'] = None
processed = []


def find_lowst(costs):
    low_cost = float("inf")
    low_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < low_cost and node not in processed:
            low_cost = cost
            low_cost_node = node
    return low_cost_node


node = find_lowst(costs)
while node is not None:
    cost = costs[node]
    friends = graph[node]
    for friend in friends.keys():
        new_cost = friends[friend] + cost

        if new_cost < costs[friend]:
            costs[friend] = new_cost
            parents[friend] = node
    processed.append(node)
    node = find_lowst(costs)
print(costs)
