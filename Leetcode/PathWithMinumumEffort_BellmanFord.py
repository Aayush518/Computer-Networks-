class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        rows, cols = len(heights), len(heights[0])
        dist = [[math.inf] * cols for _ in range(rows)]
        dist[0][0] = 0
        
        edges = []
        for i in range(rows):
            for j in range(cols):
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    x, y = i + dx, j + dy
                    if 0 <= x < rows and 0 <= y < cols:
                        edges.append((i, j, x, y, abs(heights[i][j] - heights[x][y])))

        for _ in range(rows * cols - 1):
            updated = False
            for i, j, x, y, weight in edges:
                if dist[i][j] != math.inf and max(dist[i][j], weight) < dist[x][y]:
                    dist[x][y] = max(dist[i][j], weight)
                    updated = True
            if not updated:
                break
        
        return dist[rows-1][cols-1]
