class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = "1"
        for _ in range(n - 1):
            result = self.next_sequence(result)
        return result

    def next_sequence(self, s):
        res = []
        i = 0
        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i + 1]:
                count += 1
                i += 1
            res.append(str(count) + s[i])
            i += 1
        return "".join(res)
