class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        shortest = {}

        graph = defaultdict(list)

        for u,v,weight in times:
            graph[u].append((v,weight))
        queue = [(0,k)]

        while queue:
            curr_weight,curr_node = heapq.heappop(queue)

            if curr_node in shortest:
                continue
            
            shortest[curr_node] = curr_weight

            for nbr,weight in graph[curr_node]:
                if nbr not in shortest:
                    heapq.heappush(queue,(curr_weight+weight,nbr))
        return max(shortest.values()) if len(shortest)==n else -1
