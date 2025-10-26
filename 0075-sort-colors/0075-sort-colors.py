class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s, m, e = 0, 0, len(nums)-1
        while(m<=e):
            if nums[m] == 0:
                nums[s], nums[m] = nums[m], nums[s]
                m+=1
                s+=1
            elif nums[m] == 2:
                nums[e], nums[m] = nums[m], nums[e]
                e-=1
            else:
                m+=1
        print(nums)