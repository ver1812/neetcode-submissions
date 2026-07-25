class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      n= len(nums)
      sol =[1]*n
      for i, num in enumerate(nums):
        for j, num2 in enumerate(sol):
          if j==i:
            pass
          else:
            sol[j]*=num

        
      return sol

        