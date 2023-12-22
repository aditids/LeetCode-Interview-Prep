# 2022. Convert 1D Array Into 2D Array
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original)>m*n or len(original)<m*n: return []
        result = []
        row, col = 0,0
        kth_row = []
        for i in original:
            if col<n:
               kth_row.append(i)
               col+=1
            if col == n:
                row+=1
                result.append(kth_row) 
                kth_row = []
                col = 0
        return result

        # Time and Space complexity - O(m * n)