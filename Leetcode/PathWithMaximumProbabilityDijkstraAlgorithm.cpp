#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start, int end) {
        vector<vector<pair<int, double>>> graph(n);  // {a: [(b, prob_ab)]}
        priority_queue<pair<double, int>> maxHeap;   // (prob to reach u, u)
        maxHeap.emplace(1.0, start);
        vector<bool> seen(n);

        for (int i = 0; i < edges.size(); ++i) {
            const int u = edges[i][0];
            const int v = edges[i][1];
            const double prob = succProb[i];
            graph[u].emplace_back(v, prob);
            graph[v].emplace_back(u, prob);
        }

        while (!maxHeap.empty()) {
            const auto [prob, u] = maxHeap.top();
            maxHeap.pop();
            if (u == end)
                return prob;
            if (seen[u])
                continue;
            seen[u] = true;
            for (const auto& [nextNode, edgeProb] : graph[u]) {
                if (seen[nextNode])
                    continue;
                maxHeap.emplace(prob * edgeProb, nextNode);
            }
        }

        return 0;
    }
};

int main() {
    Solution solution;
    int n = 3;
    vector<vector<int>> edges = {{0, 1}, {1, 2}, {0, 2}};
    vector<double> succProb = {0.5, 0.5, 0.2};
    int start = 0, end = 2;
    double result = solution.maxProbability(n, edges, succProb, start, end);
    cout << fixed << setprecision(5) << result << endl;
    return 0;
}