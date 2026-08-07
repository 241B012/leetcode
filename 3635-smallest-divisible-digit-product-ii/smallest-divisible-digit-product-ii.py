import collections

FACTOR_COUNTS = {
    0: collections.Counter(),
    1: collections.Counter(),
    2: collections.Counter([2]),
    3: collections.Counter([3]),
    4: collections.Counter([2, 2]),
    5: collections.Counter([5]),
    6: collections.Counter([2, 3]),
    7: collections.Counter([7]),
    8: collections.Counter([2, 2, 2]),
    9: collections.Counter([3, 3]),
}


class Solution:
    def smallestNumber(self, num: str, t: int) -> str:

        # Step 1: Factorize t using only 2, 3, 5, 7
        primeCount, possible = self.getPrimeCount(t)

        # If t has any other prime factor, impossible
        if not possible:
            return "-1"

        # Step 2: Find the minimum number of digits required
        factors = self.getFactorCount(primeCount)

        if sum(factors.values()) > len(num):
            return self.construct(factors)

        # Step 3: Count prime factors present in num
        prefix = collections.Counter()

        for ch in num:
            prefix += FACTOR_COUNTS[int(ch)]

        # First zero position
        first_zero = len(num)

        for i, ch in enumerate(num):
            if ch == '0':
                first_zero = i
                break

        # If num itself is already valid
        if first_zero == len(num) and self.isSubset(primeCount, prefix):
            return num

        # Step 4: Try changing the number from right to left
        for i in range(len(num) - 1, -1, -1):

            digit = int(num[i])

            # Remove current digit from prefix
            prefix -= FACTOR_COUNTS[digit]

            # Number of positions available after i
            space = len(num) - 1 - i

            # We cannot keep a zero before this position
            if i > first_zero:
                continue

            # Try the smallest possible bigger digit
            for bigger in range(digit + 1, 10):

                # Factors still required after using bigger
                remaining = primeCount - prefix - FACTOR_COUNTS[bigger]

                needed = self.getFactorCount(remaining)

                # Can we fit all required factors?
                if sum(needed.values()) <= space:

                    ones = space - sum(needed.values())

                    return (
                        num[:i]
                        + str(bigger)
                        + '1' * ones
                        + self.construct(needed)
                    )

        # Step 5: No answer with same length.
        # Construct the smallest answer with one extra digit.
        factors = self.getFactorCount(primeCount)

        return (
            '1' * (len(num) + 1 - sum(factors.values()))
            + self.construct(factors)
        )

    # Factorize t
    def getPrimeCount(self, t):
        count = collections.Counter()

        for p in [2, 3, 5, 7]:
            while t % p == 0:
                t //= p
                count[p] += 1

        return count, t == 1

    # Convert prime-factor requirements into digits 2...9
    def getFactorCount(self, count):

        # 2^3 = 8
        count8, remaining2 = divmod(count[2], 3)

        # 3^2 = 9
        count9, count3 = divmod(count[3], 2)

        # 2^2 = 4
        count4, count2 = divmod(remaining2, 2)

        # 2 * 3 = 6
        count6 = 0

        if count2 == 1 and count3 == 1:
            count2 = 0
            count3 = 0
            count6 = 1

        # 3 * 4 = 12 -> 2 * 6
        if count3 == 1 and count4 == 1:
            count2 = 1
            count6 = 1
            count3 = 0
            count4 = 0

        return {
            2: count2,
            3: count3,
            4: count4,
            5: count[5],
            6: count6,
            7: count[7],
            8: count8,
            9: count9
        }

    # Construct smallest string from digit counts
    def construct(self, factors):
        ans = []

        for digit in range(2, 10):
            ans.append(str(digit) * factors[digit])

        return ''.join(ans)

    # Check whether num already contains all required factors
    def isSubset(self, required, available):
        for p in [2, 3, 5, 7]:
            if available[p] < required[p]:
                return False

        return True