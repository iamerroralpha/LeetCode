#%%
from typing import List

class Solution:
    def cyclicSort(self, unorderedList: List[int]) -> List[int]:
        unorderedListLen = len(unorderedList)
        for i in range(unorderedListLen):
            complete = False
            while not complete:
                element1 = unorderedList[i]
                if element1 <= unorderedListLen:
                    if element1 != i+1:
                        element2 = unorderedList[element1-1]
                        unorderedList[element1-1] = element1
                        unorderedList[i] = element2
                    else:
                        complete = True
                else:
                    complete = True
        return unorderedList
    
#%%
class Solution:
    def cyclicSort(self, list: List[int]) -> List[int]:
        listLen = len(list)
        for i in range(listLen):
            while 1 <= list[i] <= listLen and list[i] != i + 1:
                correct_index = list[i] - 1
                list[correct_index], list[i] = list[i], list[correct_index]
        return list


#%%
input = [3,2,6,4,1]
soln = Solution()
fixed = soln.cyclicSort(input)
print(fixed)
# %%
