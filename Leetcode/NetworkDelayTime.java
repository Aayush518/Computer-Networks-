class Solution {
    public int networkDelayTime(int[][] times, int N, int K) {
        Map<Integer, List<int[]>> adjList = new HashMap<>();
        for (int[] time : times) {
            adjList.computeIfAbsent(time[0], k -> new ArrayList<>()).add(new int[]{time[1], time[2]});
        }
        
        Map<Integer, Integer> dist = new HashMap<>();
        PriorityQueue<int[]> minHeap = new PriorityQueue<>((edge1, edge2) -> {
            return edge1[1] - edge2[1];
        });
        minHeap.offer(new int[]{K, 0});
        
        while (!minHeap.isEmpty()) {
            int[] curr = minHeap.poll();
            if (dist.containsKey(curr[0])) continue;
            dist.put(curr[0], curr[1]);
            if (adjList.containsKey(curr[0])) {
                for (int[] edge : adjList.get(curr[0])) {
                    minHeap.offer(new int[]{edge[0], edge[1] + curr[1]});
                }
            }
        }
        
        if (dist.size() != N) return -1;
        int ret = Integer.MIN_VALUE;
        for (int k : dist.keySet()) {
            ret = Math.max(ret, dist.get(k));
        }
        
        return ret;
    }
}
