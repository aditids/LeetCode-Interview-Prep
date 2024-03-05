# 649. Dota2 Senate

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r, d = 0, 0
        while senate:
            rq = []
            dq = []
            q = ''
            for i in senate:
                if i=='R':
                    if r>=0:
                        d-=1
                        rq.append('R')
                        q+='R'
                    else:
                        r+=1
                    
                else:
                    if d>=0:
                        r-=1
                        dq.append('D')
                        q+='D'
                    else:
                        d+=1
            if not rq or not dq:
                if rq:
                    return 'Radiant'
                if dq:
                    return 'Dire'
            senate = q
            
        return ''      