class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dictionary = {}

        for i in range(len(order)):
            dictionary[order[i]] = i
        
        for i in range(len(words) - 1):
            l1, l2 = 0, 0
            while l1 < len(words[i]) and l2 < len(words[i + 1]):
                if dictionary[words[i][l1]] > dictionary[words[i + 1][l2]]:
                    return False
                elif dictionary[words[i][l1]] < dictionary[words[i + 1][l2]]:
                    break
                else:
                    l1 += 1
                    l2 += 1
            
            if l1 < len(words[i]) and l2 == len(words[i + 1]):
                return False

        
        return True
