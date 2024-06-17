# 909. Snakes and Ladders

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        board.reverse()
        # print(board)
        def getCoordinates(sq):
            r = (sq-1)//n
            c = (sq - 1)%n
            if r%2:
                c = n - 1 - c
            return [r,c]
        q = [[1,0]]     # [square, move]
        visit = set()
        while q:
            cur, count = q.pop(0)
            for i in range(1,7):
                nxt = cur+i
                r,c = getCoordinates(nxt)
                
                if board[r][c]!=-1:
                    nxt = board[r][c]
                if nxt == n**2:
                    return count+1
                if nxt not in visit:
                    visit.add(nxt)
                    q.append([nxt,count+1])
            
        return -1