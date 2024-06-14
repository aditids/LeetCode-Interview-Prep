# 68. Text Justification

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        i = 0

        while i<len(words):
            current_words = self.getWords(words, i, maxWidth)
            i+=len(current_words)
            current_line = self.createLine(current_words, i, maxWidth, len(words))
            result.append(current_line)
        return result

    def getWords(self, words, i, maxWidth):
        current_words = []
        current_length = 0

        while i<len(words) and maxWidth >= current_length + len(words[i]):
            current_length+= len(words[i])+1
            current_words.append(words[i])
            i+=1
        return current_words

    def createLine(self, words, i, maxWidth, k):
        minLength = -1
        for word in words:
            minLength += len(word) + 1
        
        extra_space = maxWidth - minLength
        if len(words) == 1 or i == k:
            return ' '.join(words) + ' '* extra_space

        n = len(words) - 1
        space = extra_space // n
        left_space = extra_space % n
        for j in range(left_space):
            words[j] += ' '

        for j in range(n):
            words[j] += ' '* space
        return ' '.join(words) 