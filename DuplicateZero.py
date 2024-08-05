from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        length = len(arr)
        zeros_to_duplicate = arr.count(0)

        # Trabalhar do final para o início
        for i in range(length - 1, -1, -1):
            if arr[i] == 0:
                # Se houver espaço para duplicar o zero
                if i + zeros_to_duplicate < length:
                    arr[i + zeros_to_duplicate] = 0
                zeros_to_duplicate -= 1
                # Após duplicar o zero, verifique se há espaço para a segunda cópia
                if i + zeros_to_duplicate < length:
                    arr[i + zeros_to_duplicate] = 0
            else:
                if i + zeros_to_duplicate < length:
                    arr[i + zeros_to_duplicate] = arr[i]

# Exemplo de uso
sol = Solution()
arr = [1, 0, 2, 3, 0, 4, 5, 0]
sol.duplicateZeros(arr)
print(arr)  # Saída esperada: [1, 0, 0, 2, 3, 0, 0, 4]
