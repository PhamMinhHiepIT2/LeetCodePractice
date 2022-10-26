from typing import List

INF = float('inf')


class Solution:
    def shortest_path(self, n: int, shortest_paths: List[int], neighbor: List[List[int]], visited: List[int], start: int, end: int):
        # visited[start] = True
        visited.append(start)
        # visited_index = []
        # for i in range(len(visited)):
        #     if visited[i]:
        #         visited_index.append(i)
        # print(f'---- SP from {visited_index + [start]} to {end} ----')
        # print(f'---- shortest_paths {shortest_paths} ----')
        # print(f'---- visited {visited} ----')

        if start == end:
            return 0
        if shortest_paths[start] is not None:
            return shortest_paths[start]
        if start not in neighbor:
            return INF
        cur_neighbor = neighbor[start]
        # print(f'----- neighbor of {start} {cur_neighbor} ------')
        available_short_paths = []
        for nb in cur_neighbor:
            print(
                f' checking {visited} - {[nb["target"]]} ({nb["distance"]} with vi')
            if nb["target"] in visited:
                continue
            tmp_shortest_paths = shortest_paths.copy()
            tmp_visited = visited.copy()
            a = nb["distance"] + self.shortest_path(
                n, tmp_shortest_paths, neighbor, tmp_visited, nb["target"], end)
            available_short_paths.append(a
                                         )
            print(
                f' short from {tmp_visited} - {[nb["target"]]} ({nb["distance"]}) to {end} is {a}')
        if not available_short_paths:
            return INF
        # print(f'available_short_paths {available_short_paths}')
        result = min(available_short_paths)
        shortest_paths[start] = result
        print(f'---- SP from {start} to {end} is {result} ----')
        return result

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        MAX = 100*n + 1
        neighbor = {}
        for time in times:
            if time[0] not in neighbor:
                neighbor[time[0]] = []
            neighbor[time[0]].append({
                "target": time[1],
                "distance": time[2]
            })
        print(f'neighbor {neighbor}')
        shortest_paths = [None for _ in range(n+1)]
        paths = []
        for i in range(1, n+1):
            print(f'--- Shortest from {k} to {i} ---')
            # visited = [False for _ in range(n+1)]
            visited = []
            weight = self.shortest_path(
                n, shortest_paths, neighbor, visited, k, i)
            print(f'--- Shortest from {k} to {i} is {weight}---')
            if weight > MAX:
                return -1
            paths.append(weight)
        return max(paths)


sol = Solution()

test_cases = [
    # dict(
    #     times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]],
    #     n=4,
    #     k=2,
    #     result=2
    # ),
    # dict(
    #     times=[[2, 1, 1], [2, 3, 1], [3, 1, 1], [2, 4, 1]],
    #     n=4,
    #     k=2,
    #     result=1
    # ),
    # dict(
    #     times=[[1,2,1]],
    #     n=2,
    #     k=1,
    #     result=1
    # ),
    # dict(times = [[1,2,1]], n = 2, k = 2, result=-1),
    # dict(
    #     times=[[1, 2, 1], [2, 3, 7], [1, 3, 4], [2, 1, 2]],
    #     n=3,
    #     k=1, result=8
    # ),
    # dict(
    #     times=[[1,2,1],[2,3,2],[1,3,2]],
    #     n=3,
    #     k=1,
    #     result=2
    # ),
    dict(
        times=[[4, 2, 76], [1, 3, 79], [3, 1, 81], [4, 3, 30], [2, 1, 47], [1, 5, 61], [1, 4, 99], [3, 4, 68], [3, 5, 46], [4, 1, 6], [
            5, 4, 7], [5, 3, 44], [4, 5, 19], [2, 3, 13], [3, 2, 18], [1, 2, 0], [5, 1, 25], [2, 5, 58], [2, 4, 77], [5, 2, 74]],
        n=5,
        k=3,
        result=59
    ),
]

for i, input in enumerate(test_cases):
    print(f'---------------- test case [{i}] -----------------')
    print(input)
    print(f'--------------------------------------------------')
    result = input.pop('result')
    ans = sol.networkDelayTime(**input)
    # ans = sol.merge_max([6,7,0], [6])
    print(f' ans = {ans}')
    if ans == result:
        print('>>>>>>>> PASS <<<<<<<<')
    else:
        print('<<<<<<<<<<<<<<<<<<< FAILED >>>>>>>>>>>>>>>>>>')
