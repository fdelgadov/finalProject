def dijkstra(graph, vertex):
  distances = [INF for i in graph]
  distances[vertex] = 0
  queue = [vertex]
  route = [-1 for i in graph]

  while len(queue) > 0:
    actual = queue[0]
    for i in range(1, len(queue)):
      if distances[actual] > distances[queue[i]]:
        actual = queue[i]
    queue.remove(actual)

    i = 0
    for edge in graph[actual]:
      if edge != INF and edge + distances[actual] < distances[i]:
        distances[i] = edge + distances[actual]
        queue.append(i)
        route[i] = actual

      i += 1

  return [distances, route]

def floydWarshall(graph):
  length = len(graph)
  dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
  for k in range(length):
    for i in range(length): 
      for j in range(length):
        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

  return dist

def BellmanFord(graph, vertex):
  length = len(graph)
  dist = [INF] * length
  dist[vertex] = 0

  for _ in range(length - 1):
    for i in range(length):
      for j in range(length):
        if graph[i][j] != INF:
          if dist[i] != INF and dist[i] + graph[i][j] < dist[j]:
            dist[j] = dist[i] + graph[i][j]

  for i in range(length):
    for j in range(length):
      if graph[i][j] != INF:
        if dist[i] != INF and dist[i] + graph[i][j] < dist[j]:
          print("Contiene ciclo negativo")
          return

  return dist

INF = float("inf")
graph = [
  [0, 4, INF, INF, 2, INF, INF, INF],
  [INF, 0, 1, INF, INF, INF, INF, INF],
  [INF, INF, 0, 5, 3, INF, INF, INF],
  [INF, INF, INF, 0, INF, INF, 2, 1],
  [INF, 1, INF, INF, 0, 2, INF, INF],
  [INF, INF, 6, 3, INF, 0, 3, INF],
  [INF, INF, INF, INF, INF, INF, 0, 7],
  [INF, INF, INF, INF, INF, INF, INF, 0],
]
print(f'dijkstra: {dijkstra(graph, 0)}')
print(f'dijkstra: {dijkstra(graph, 7)}')
print(f'dijkstra: {dijkstra(graph, 2)}')

print(f'floy-warshall(graph): {floydWarshall(graph)}')
print(f'bellmanFord(graph): {BellmanFord(graph, 0)}')
print(f'bellmanFord(graph): {BellmanFord(graph, 7)}')
print(f'bellmanFord(graph): {BellmanFord(graph, 2)}')