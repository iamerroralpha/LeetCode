#%% Description
Example 1:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]

#%%
from typing import List
from collections import defaultdict
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        output = []
        character_counts = defaultdict(int)
        for element1 in words2:
            ind_characters = defaultdict(int)
            for element2 in element1:
                ind_characters[element2] += 1
            for element in ind_characters:
                character_counts[element] = max(character_counts[element], ind_characters[element])

        for element1 in words1:
            character_counts1 = defaultdict(int)
            for element2 in element1:
                character_counts1[element2] += 1
            if all(character_counts1[char] >= character_counts[char] for char in character_counts):
                output.append(element1)
        return output
    

#%%
mySolution = Solution()

#Test1
#words1 = ["amazon","apple","facebook","google","leetcode"]
#words2 = ["e","o"]
#Test2
#words1 = ["amazon","apple","facebook","google","leetcode"]
#words2 = ["lo","eo"]
words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["e","oo"]
output = mySolution.wordSubsets(words1, words2)
print(output)
# %%
from collections import Counter
from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # Precompute maximum frequency of each character across all words in words2
        max_freq = Counter()
        for word in words2:
            word_count = Counter(word)
            for char, freq in word_count.items():
                max_freq[char] = max(max_freq[char], freq)
        
        # Check each word in words1 against the precomputed frequencies
        output = []
        for word in words1:
            word_count = Counter(word)
            if all(word_count[char] >= freq for char, freq in max_freq.items()):
                output.append(word)
        
        return output