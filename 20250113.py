#%%

class Solution:
    def minimumLength(self, s: str) -> int:
        counts  = [0 for _ in range(26)]
        for element in s:
            elementord = ord(element) - ord('a')
            counts[elementord] += 1

        new_len = 0

        for element in counts:
            if element % 2 == 1:
                new_len += 1
            elif element !=0:
                new_len += 2

        return new_len


#%%
soln = Solution()
input = "abaacbcbb" 
print(soln.minimumLength(input))
#%%

Example 1:

Input: s = "abaacbcbb"

Output: 5

Explanation:
We do the following operations:

Choose index 2, then remove the characters at indices 0 and 3. The resulting string is s = "bacbcbb".
Choose index 3, then remove the characters at indices 0 and 5. The resulting string is s = "acbcb".