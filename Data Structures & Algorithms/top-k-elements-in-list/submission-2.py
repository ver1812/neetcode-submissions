from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        new = Counter(nums)
        return [num for num,freq in new.most_common(k)]

            


        