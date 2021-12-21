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

def interpretRoute(route, goal):
  last = route[goal]
  out = [goal]
  while True:
    if last == -1:
      break
    out.insert(0, last)
    last = route[last]
  
  return out

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

def display(arr):
  res = f'{arr[0]}'
  for row in arr[1:]:
    res = f'{res}\n{row}'
  
  return res

INF = float("inf")
graph = [
   #                                       HA   HyO  HcO   HZ   IA   IS  LA   MA                        
  [0  , 655, 385, INF, INF, INF, INF, 193, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,],
  [655,   0, 981, INF, INF, INF, INF, 613, INF, INF, INF, INF, 712, INF, INF, INF, 223, INF, INF, INF, 293, INF, INF, INF,],
  [385, 981,   0, INF, INF, INF, INF, INF, 203, 260, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,],
  [INF, INF, INF,   0, INF, 355, 255, INF, INF, INF, INF, INF, INF, INF, INF, 671, INF, INF, INF, INF, INF, INF, 298, INF,],

  [INF, INF, INF, INF,   0, INF, INF, INF, 340, 256, 102, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,],
  [INF, INF, INF, 355, INF,   0, INF, INF, INF, INF, INF, INF, INF, INF, INF, 254, INF, INF, INF, INF, INF, INF, INF, INF,],
  [INF, INF, INF, 255, INF, INF,   0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 220, INF, INF, INF, INF, 211, INF,],
  [193, 613, INF, INF, INF, INF, INF,   0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,1196, 478, 386, INF, INF, INF,],

  [INF, INF, 203, INF, INF, INF, INF, INF,   0, 144, 496, INF, 340, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,],
  [INF, INF, 260, INF, 256, INF, INF, INF, 144,   0, INF, INF, INF, INF, 305, INF, INF, INF, 597, INF, INF, INF, INF, INF,],
  [INF, INF, INF, INF, 102, INF, INF, INF, 496, INF,   0, 326, INF, INF, INF, 717, INF, INF, 371, INF, INF, INF, INF, INF,],
  [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 326,   0, INF, INF, INF, 883, INF, INF, INF, INF, INF, INF, 313, INF,],
  #--
  [INF, 712, INF, INF, INF, INF, INF, INF, 340, INF, INF, INF,   0, INF, 297, INF, INF, INF, INF, INF, INF, INF, INF, INF,],
  [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,],
  [INF, INF, INF, INF, INF, INF, INF, INF, INF, 305, INF, INF, 297, INF,   0, INF, INF, INF, INF, INF, INF, INF, INF, INF,],
  [INF, INF, INF, INF, INF, 254, INF, INF, INF, INF, 717, 883, INF, INF, INF,   0, INF, INF, 816, INF, INF, INF, INF, INF,],
  #--
  [INF, 223, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   0, INF, INF, INF, 266, 160, INF, INF,],
  [INF, INF, INF, INF, INF, INF, 220, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   0, INF, INF, INF, INF, INF, 285,],
  [INF, INF, INF, INF, INF, INF, INF,1196, INF, 597, 371, INF, INF, INF, INF, 816, INF, INF,   0,1629, INF, INF, INF, INF,],
  [INF, INF, INF, INF, INF, INF, INF, 478, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,1629,   0, 605, INF, INF, INF,],
  
  [INF, 293, INF, INF, INF, INF, INF, 386, INF, INF, INF, INF, INF, INF, INF, INF, 266, INF, INF, 605,   0, 368, INF, INF,],
  [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 160, INF, INF, INF, 368,   0, INF, INF,],
  [INF, INF, INF, 298, INF, INF, 211, INF, INF, INF, INF, 313, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   0, INF,],
  [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 285, INF, INF, INF, INF, INF,   0,],
]
"""
print(f'dijkstra: {dijkstra(graph, 0)}')
print(f'dijkstra: {dijkstra(graph, 7)}')
print(f'dijkstra: {dijkstra(graph, 2)}')

print(f'floy-warshall(graph): {floydWarshall(graph)}')
print(f'bellmanFord(graph): {BellmanFord(graph, 0)}')
print(f'bellmanFord(graph): {BellmanFord(graph, 7)}')
print(f'bellmanFord(graph): {BellmanFord(graph, 2)}')
"""