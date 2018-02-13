class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        first = strs.pop()
        for i in range(len(first)):
            c = first[i]
            for j in range(len(strs)):
                if i == len(strs[j]) or strs[j][i] != c:
                    return first[:i]      
        return first
if __name__ == "__main__":
    s = Solution()
    result = s.longestCommonPrefix(['cat','cata',"catapillar"])
    print(result)