class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        rows, cols = len(heights), len(heights[0])
        dist = [[math.inf] * cols for _ in range(rows)]  # Initialize distances to infinity
        dist[0][0] = 0  # Starting cell has 0 effort

        minHeap = [(0, 0, 0)]  # (effort, row, col)

        while minHeap:
            d, i, j = heapq.heappop(minHeap)  # Get cell with min effort
            if i == rows - 1 and j == cols - 1:  # Reached destination
                return d

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # Explore neighbors
                x, y = i + dx, j + dy
                if 0 <= x < rows and 0 <= y < cols:  # Check if neighbor is valid
                    new_effort = max(d, abs(heights[i][j] - heights[x][y]))  # Calculate effort
                    if new_effort < dist[x][y]:  # If lower effort found
                        dist[x][y] = new_effort
                        heapq.heappush(minHeap, (new_effort, x, y))  # Add to heap
