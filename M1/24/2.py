from collections import deque

graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6],
}


def bfs(graph, start):
    visited = set()  # Множество для посещённых вершин
    queue = [start]  # Очередь для вершин на текущем уровне
    visited.add(start)  # Добавляем стартовую вершину
    while queue:
        vertex = queue.pop(0)  # Берём вершину из начала очереди
        print(f"Посещаем вершину: {vertex}")
        # Добавляем все смежные вершины в очередь
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited


def bfs2(start):
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node)
            visited.add(node)
            queue += graph[node]
    return visited


print(bfs2(1))

