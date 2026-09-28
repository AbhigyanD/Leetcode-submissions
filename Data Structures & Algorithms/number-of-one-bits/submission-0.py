class Solution:
    def hammingWeight(self, n: int) -> int:
        r = f"{n:b}"
        c = 0
        for ch in r:
            if ch == "1":
                c = c+1

        return c