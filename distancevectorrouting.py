INF = 999

# Cost matrix
cost = [
    [0, 1, 4, INF],
    [1, 0, INF, 2],
    [4, INF, 0, 1],
    [INF, 2, 1, 0]
]

n = len(cost)

# Distance table
dist = [row[:] for row in cost]

# Next-hop table
next_hop = [[j if cost[i][j] != INF and i != j else -1
             for j in range(n)] for i in range(n)]

# Distance Vector Algorithm
updated = True

while updated:
    updated = False

    for i in range(n):
        for j in range(n):
            for k in range(n):

                if dist[i][k] != INF and dist[k][j] != INF:
                    new_distance = dist[i][k] + dist[k][j]

                    if new_distance < dist[i][j]:
                        dist[i][j] = new_distance
                        next_hop[i][j] = next_hop[i][k]
                        updated = True

# Display routing tables
nodes = ['A', 'B', 'C', 'D']

for i in range(n):
    print("\nRouting Table for Router", nodes[i])
    print("Destination\tCost\tNext Hop")

    for j in range(n):
        if i == j:
            print(nodes[j], "\t\t0\t-")
        else:
            print(nodes[j], "\t\t", dist[i][j],
                  "\t", nodes[next_hop[i][j]])