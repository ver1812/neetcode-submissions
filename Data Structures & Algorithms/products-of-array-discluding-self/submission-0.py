class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      sol =[]
      for i, num in enumerate(nums):
        pro = 1
        temp = nums.copy()
        temp.pop(i)
        for number in temp:
          pro *= number
        sol.append(pro)
      return sol

        