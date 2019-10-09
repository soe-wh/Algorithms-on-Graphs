#Uses python3

import sys


def number_of_components(adj):
    result = 0
    # write your code here
    visited = [0] * len(adj)
    for i in xrange(len(adj)):
        if not visited[i]:
            explore(adj, i, visited)
            result += 1
    return result


def explore(adj, x, visited):
    visited[x] = 1
    for i in xrange(len(adj[x])):
        if not visited[adj[x][i]]:
            explore(adj, adj[x][i], visited)

    print(number_of_components(adj))


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
