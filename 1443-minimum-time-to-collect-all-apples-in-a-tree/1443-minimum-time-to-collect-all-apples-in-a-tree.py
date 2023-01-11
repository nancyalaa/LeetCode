class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = {i: [] for i in range(n)}
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
        def dfs(node, parent):
            time = 0
            for child in tree[node]:
                if child != parent:
                    time += dfs(child, node)
            if (time or hasApple[node]) and node != 0:
                time += 2
            return time
        return dfs(0, None)