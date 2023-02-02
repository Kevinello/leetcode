from typing import List


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # 整理临接表
        graph = [[] for _ in range(n)]
        for node_number, next_node in redEdges:
            graph[node_number].append((next_node, 0))
        for node_number, next_node in blueEdges:
            graph[node_number].append((next_node, 1))

        min_paths_len = [-1] * n
        visited = {(0, 0), (0, 1)}
        to_search = [(0, 0), (0, 1)]
        search_level = 0
        while to_search:
            cur_search = to_search
            to_search = []
            for node_number, color in cur_search:
                if min_paths_len[node_number] == -1:
                    min_paths_len[node_number] = search_level
                for edge in graph[node_number]:
                    if edge[1] != color and edge not in visited:
                        visited.add(edge)
                        to_search.append(edge)
            search_level += 1
        return min_paths_len