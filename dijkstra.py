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