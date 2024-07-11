class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        # Build adjacency list for the graph
        graph = defaultdict(list)
        for u, v, price in flights:
            graph[u].append((v, price))  # Store (destination, price) for each city

        # Priority queue for Dijkstra with stops: (cost, city, stops)
        pq = [(0, src, 0)]  # Start at source with 0 cost and 0 stops
        min_cost = defaultdict(lambda: float('inf'))
        min_cost[(src, 0)] = 0  # Base case: 0 cost to reach source with 0 stops

        while pq:
            cost, current_city, stops = heappop(pq)
            if current_city == dst:
                return cost  # Found destination

            if stops <= k:  # Explore further only if within stop limit
                for neighbor, price in graph[current_city]:
                    new_cost = cost + price
                    # Update if this path is cheaper for the given stops
                    if new_cost < min_cost[(neighbor, stops + 1)]: 
                        min_cost[(neighbor, stops + 1)] = new_cost
                        heappush(pq, (new_cost, neighbor, stops + 1))

        return -1  # No path found within the allowed stops
