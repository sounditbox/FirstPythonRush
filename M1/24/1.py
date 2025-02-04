graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9],
}


def dfs(g, start, visited=None):
    if visited is None:
        visited = set()  # Множество для хранения посещённых вершин
    visited.add(start)  # Добавляем начальную вершину в посещённые
    print(start)  # Выводим посещённую вершину
    # Рекурсивно проходим по всем смежным вершинам
    for adj_node in g[start]:
        if adj_node not in visited:
            # Рекурсивно вызываем DFS для каждой смежной вершины
            dfs(g, adj_node, visited)
    return visited  # Возвращаем множество посещённых вершин


def dfs_iterative(start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node)
            visited.add(node)
            stack += reversed(graph[node])
    return visited


# print(dfs(graph, 1))
print(dfs_iterative(1))
