class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1: return 1
        map = {}
        max_string, temp = "", ""
        max_len = 0
        for index, char in enumerate(s):
            if char in map:
                for i in range(len(temp)):
                    if temp[i] == char:
                        temp = temp[i+1:]
                        break
            map[char] = index
            temp += char
            if len(temp) > max_len:
                max_string = temp
                max_len = len(temp)
        return max_len
