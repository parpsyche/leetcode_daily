class Solution:
    def longestPalindrome(self, s: str) -> str:
        resindex, reslen = 0, 0
        n = len(s)
        for i in range(n):
            l,r = i,i
            while l>=0 and r<n and s[l] == s[r]:
                if r-l+1 > reslen: 
                    reslen = r-l+1
                    resindex = l
                l-=1
                r+=1
            
            l,r = i, i+1
            while l>=0 and r<n and s[l] == s[r]:
                if r-l+1 > reslen: 
                    reslen = r-l+1
                    resindex = l
                l-=1
                r+=1
            
        return s[resindex:resindex+reslen]
            
