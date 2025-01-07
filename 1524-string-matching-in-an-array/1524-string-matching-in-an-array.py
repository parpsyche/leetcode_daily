class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = set()
        for index, i in enumerate(words):
            for ind, j in enumerate(words):
                if index != ind:
                    if i in j:
                        res.add(i)
        
        return list(res)