from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        arr = [0]*(len(nums)+1)
        for num, count in counter.items():
            if arr[count] == 0:
                arr[count] = []
            arr[count].append(num)
        
        res = []
        for i in range(len(arr)-1,0,-1):
            if isinstance(arr[i], list): res.extend(arr[i])
            if len(res) >= k:
                return res[:k+1] 