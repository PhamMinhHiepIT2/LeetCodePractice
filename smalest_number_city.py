from typing import List
import heapq

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        G = get_neighbor(edges, n)
        paths, weights = find_all_shortest_path(G, n, distanceThreshold)
        st = []
        for i in range(len(paths)):
            p = paths[i]
            w = weights[i]
            not_null, valid_ids = count_valid(p, w, distanceThreshold)
            sum_p = sum_arr(w, distanceThreshold, valid_ids)
            print(f"Node: {i} | Count valid: {not_null} | Valid index: {valid_ids} | Sum array: {sum_p}")
            
            st.append((not_null, sum_p, i))
        st.sort(key=lambda x: x[0])
        print(f"----> Sorted Stack: {st}")
        cur = st[0]
        for el in st:
            if el == cur:
                continue
            if el[0] == cur[0] and el[1] < cur[1]:
                cur = el
        return cur[2]




def get_neighbor(edges: List[List[int]], n):
    G = [[] for _ in range(n)]
    for edge in edges:
        source = edge[0]
        destination = edge[1]
        distance = edge[2]
        G[source].append((destination, distance))
        G[destination].append((source, distance))
    return G


def dijkstra(G, s, n, distanceThreshold):
    visited = [False] * n
    weights = [float('inf')] * n
    path = [None] * n
    weights[s] = 0
    queue = []
    heapq.heappush(queue, (0, s))
    while len(queue) > 0:
        cur_weight, u = heapq.heappop(queue)
        visited[u] = True
        for v, w in G[u]:
            if not visited[v]:
                new_weight = cur_weight + w
                if new_weight < weights[v]:
                    weights[v] = new_weight
                    path[v] = u
                    heapq.heappush(queue, (new_weight, v))
    return path, weights

def dijkstra_heap(G, s):
    n = len(G)
    distance = [float('inf') for _ in range(n)]
    heap = []
    heapq.heappush(heap, (0, s))
    visited = [False for _ in range(n)]

    while heap:
        dist, node = heapq.heappop(heap)
        if visited[node] == True:
            continue
        visited[node] = True
        for neighbor, weight in G[node]:
            if visited[neighbor] == False:
                new_weight = dist + weight
                if new_weight < distance[neighbor] and new_weight <= distanceThreshold:
                    distance[neighbor] = new_weight
                    heapq.heappush(heap, (new_weight, neighbor))
    return distance

def find_all_shortest_path(G, n, distanceThreshold):
    paths = []
    weights = []
    for i in range(n):
        path, weight = dijkstra(G, i, n, distanceThreshold)
        print(f"Vertex: {i} | path: {path} | weights: {weight}")
        paths.append(path)
        weights.append(weight)
    return paths, weights


def count_valid(paths: list, weights: list, distanceThreshold: int):
    res = 0
    valid_ids = []
    for i in range(len(paths)):
        if paths[i] != None and weights[i] <= distanceThreshold:
            res += 1
            valid_ids.append(i)
    return res, valid_ids

def sum_arr(arr: list, distanceThreshold: int, valid_ids: list):
    res = 0
    for i in range(len(arr)):
        if i in valid_ids:
            res += arr[i]

    return res

if __name__ == "__main__":
    n = 6
    edges = [[0,3,5],[2,3,7],[0,5,2],[0,2,5],[1,2,6],[1,4,7],[3,4,4],[2,5,5],[1,5,8]]


    distanceThreshold = 8279

    print(Solution().findTheCity(n, edges, distanceThreshold))
    print("=-=========================")
    G = get_neighbor(edges, n)
    print(G)
    print(dijkstra_heap(G, 0))


6

8279