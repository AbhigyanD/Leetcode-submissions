class Solution:
    def countBits(self, n: int) -> List[int]:
        
        res = [0] * (n + 1)
        lastval = 1

        for i in range(1, n + 1):
            if lastval * 2 == i:
                lastval = i
            
            res[i] = 1 + res[i - lastval]
        
        return res