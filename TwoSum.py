from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numeros = {}
        
        for i, numero in enumerate(nums):
            complemento = target - numero
            
            if complemento in numeros:
                return [numeros[complemento], i]
            
            numeros[numero] = i
        
        return None

# Exemplo de uso
nums = [2, 7, 11, 15]
target = 9
solucao = Solution()
resultado = solucao.twoSum(nums, target)
if resultado:
    print(resultado)  # Output: [0, 1]
else:
    print("false")
