from bisect import bisect_left, bisect_right

class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n = len(word1)
        m = len(word2)

        # Store all positions of each character in word1
        pos = {}

        for i, ch in enumerate(word1):
            if ch not in pos:
                pos[ch] = []
            pos[ch].append(i)

        # ---------------------------------------------------------
        # run_start[i] = start of the same-character block containing i
        # run_end[i]   = end of the same-character block containing i
        # ---------------------------------------------------------

        run_start = [0] * n
        run_end = [0] * n

        start = 0
        for i in range(n):
            if i == 0 or word1[i] != word1[i - 1]:
                start = i
            run_start[i] = start

        end = n - 1
        for i in range(n - 1, -1, -1):
            if i == n - 1 or word1[i] != word1[i + 1]:
                end = i
            run_end[i] = end

        # ---------------------------------------------------------
        # exact[k] = latest possible position of word2[k]
        #           when word2[k:] is matched EXACTLY.
        #
        # one[k] = latest possible position of word2[k]
        #          when word2[k:] is matched with <= 1 mismatch.
        # ---------------------------------------------------------

        exact = [-1] * (m + 1)
        one = [-1] * (m + 1)

        # Empty suffix can start after the last character
        exact[m] = n
        one[m] = n

        # Build exact[] and one[] from right to left
        for k in range(m - 1, -1, -1):
            ch = word2[k]
            positions = pos.get(ch, [])

            # -------------------------
            # Calculate exact[k]
            # -------------------------
            limit = exact[k + 1]

            if limit > 0 and positions:
                p = bisect_left(positions, limit) - 1

                if p >= 0:
                    exact[k] = positions[p]

            # -------------------------
            # Calculate one[k]
            # -------------------------
            best = -1

            # Case 1:
            # word1[k] matches word2[k]
            # and the remaining suffix uses <= 1 mismatch.
            limit = one[k + 1]

            if limit > 0 and positions:
                p = bisect_left(positions, limit) - 1

                if p >= 0:
                    best = positions[p]

            # Case 2:
            # word1[k] is the ONE mismatch,
            # so the remaining suffix must match exactly.
            limit = exact[k + 1]

            if limit > 0:
                idx = limit - 1

                if word1[idx] != ch:
                    candidate = idx
                else:
                    # idx is part of a block of ch.
                    # The character immediately before that block
                    # is the latest position having a different char.
                    candidate = run_start[idx] - 1

                best = max(best, candidate)

            one[k] = best

        # ---------------------------------------------------------
        # Construct lexicographically smallest answer
        # ---------------------------------------------------------

        ans = []
        prev = -1
        mismatch_used = False

        for k in range(m):
            ch = word2[k]

            # =====================================================
            # If mismatch is already used:
            # We MUST match the remaining characters exactly.
            # =====================================================
            if mismatch_used:

                positions = pos.get(ch, [])
                limit = exact[k + 1]

                p = bisect_right(positions, prev)

                if p >= len(positions):
                    return []

                j = positions[p]

                # Must leave enough room for the exact suffix
                if j >= limit:
                    return []

            # =====================================================
            # Mismatch is still available
            # =====================================================
            else:

                best = n

                # -------------------------------------------------
                # Option 1: Match word2[k]
                # -------------------------------------------------
                positions = pos.get(ch, [])
                limit = one[k + 1]

                p = bisect_right(positions, prev)

                if p < len(positions):
                    j = positions[p]

                    if j < limit:
                        best = j

                # -------------------------------------------------
                # Option 2: Use mismatch at this position
                # -------------------------------------------------
                start = prev + 1

                if start < n:

                    if word1[start] != ch:
                        candidate = start
                    else:
                        # Skip the entire block of the same character
                        candidate = run_end[start] + 1

                    # After using mismatch, suffix must match exactly
                    if candidate < n and candidate < exact[k + 1]:
                        best = min(best, candidate)

                if best == n:
                    return []

                j = best

            # Add selected index
            ans.append(j)

            # Check whether mismatch was used
            if word1[j] != ch:
                mismatch_used = True

            prev = j

        return ans