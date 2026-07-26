class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for num in numbers:
            rem = target-num
            if rem in numbers:
                return [numbers.index(num)+1,numbers.index(rem)+1]

        