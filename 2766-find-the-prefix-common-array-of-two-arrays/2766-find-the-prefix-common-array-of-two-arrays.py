class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        setA = set(A)
        setB = set(B)
        for i in range(len(A)-1 , -1, -1):
            diff = len(setA.intersection(setB))
            res.insert(0, diff)
            setA.remove(A[i])
            setB.remove(B[i])
        return res