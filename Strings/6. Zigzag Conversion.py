# 6. Zigzag Conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)

        if numRows == 1 or n==1 or n<numRows:
            return s

        row = ceil(n/(2*numRows-2))
        col = row * (numRows-1)

        matrix = [[''] * col for _ in range(numRows)]

        r, c = 0, 0
        cur = 0

        while cur<n:
            while r < numRows and cur<n:
                matrix[r][c] = s[cur]
                r += 1
                cur += 1

            r -= 2
            c += 1

            while r > 0 and c < col and cur < n:
                matrix[r][c] = s[cur]
                r -= 1
                c += 1
                cur += 1

        res = ''
        for i in matrix:
            res += ''.join(i)

        return res