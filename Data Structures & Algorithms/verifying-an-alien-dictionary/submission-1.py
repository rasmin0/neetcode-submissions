class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderMap = {}
        for i in range(len(order)):
            if order[i] not in orderMap:
                orderMap[order[i]] = i
        
        for i in range(len(words) - 1):
            l1, l2 = 0, 0

            while l1 < len(words[i]) and l2 < len(words[i + 1]):
                if orderMap[words[i][l1]] > orderMap[words[i + 1][l2]]:
                    return False
                elif orderMap[words[i][l1]] == orderMap[words[i + 1][l2]]:
                    l1 += 1
                    l2 += 1
                else:
                    break
            
            if l1 < len(words[i]) and l2 == len(words[i + 1]):
                return False
        
        return True
