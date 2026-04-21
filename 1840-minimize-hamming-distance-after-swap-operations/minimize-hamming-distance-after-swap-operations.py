from collections import defaultdict, Counter

class Solution:
    def minimumHammingDistance(self, source, target, allowedSwaps):
        parent = list(range(len(source)))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px

        # Step 1: Build components
        for a, b in allowedSwaps:
            union(a, b)

        # Step 2: Group indices by root
        groups = defaultdict(list)
        for i in range(len(source)):
            root = find(i)
            groups[root].append(i)

        # Step 3: Count matches
        hamming = 0

        for indices in groups.values():
            freq = Counter()
            
            # count source values
            for i in indices:
                freq[source[i]] += 1
            
            # match with target
            for i in indices:
                if freq[target[i]] > 0:
                    freq[target[i]] -= 1
                else:
                    hamming += 1

        return hamming