class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        # Step 1: Initialize distances array with infinity and set source distance to 0
        inf = float('inf')
        dist = [inf] * n 
        dist[src] = 0

        # Step 2: Relax edges for k + 1 times
        for _ in range(k + 1):  # Iterate for the number of allowed stops + 1
            current_dist = dist[:]

            for u, v, w in flights:  # Relax all edges (u, v, w)
                if dist[u] != inf and dist[u] + w < current_dist[v]:
                    current_dist[v] = dist[u] + w  # Update if a cheaper path is found

            dist = current_dist  # Update distances for the next iteration

        # Step 3: Return the shortest distance to dst, or -1 if not reachable
        return dist[dst] if dist[dst] != inf else -1  

