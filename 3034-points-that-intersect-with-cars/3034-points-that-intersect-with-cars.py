class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        points = [0]*102
        for start, end  in nums:
            points[start] +=1
            points[end+1] -=1
        
        res, pos = 0, 0
        for point in points:
            pos += point
            if pos>=1:
                res+=1
        
        return res