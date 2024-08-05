from typing import List

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        # Verificar se os valores fornecidos podem formar um triângulo
        if nums[0] + nums[1] <= nums[2] or nums[1] + nums[2] <= nums[0] or nums[0] + nums[2] <= nums[1]:
            return "none"
        
        if nums[0] == nums[1] == nums[2]:
            return "equilateral"
        elif nums[0] != nums[1] and nums[1] != nums[2] and nums[0] != nums[2]:
            return "scalene"
        else:
            return "isosceles"
        
solution = Solution()
list = [8, 4, 2]
result = solution.triangleType(list)
print(result)
