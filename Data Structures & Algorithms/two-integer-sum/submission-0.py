class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, number in enumerate(nums):

            need = target - number
            if need in seen:
                return [seen[need],i]
            
            if number not in seen:
                seen[number]=i

        