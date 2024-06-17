# 127. Word Ladder

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        adjList = defaultdict(list)
        q = deque([beginWord])
        visit = set([beginWord])
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                adjList[pattern].append(word)
        
        count = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return count
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    for k in adjList[pattern]:
                        if k not in visit:
                            visit.add(k)
                            q.append(k)
            count+=1
        return 0