class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        """
        :type n: int
        :rtype: bool
        """
        # Verifica se o número é maior que zero e se é uma potência de 3
        if n <= 0:
            return False
        
        # Divide n por 3 até que não seja mais divisível
        while n % 4 == 0:
            n //= 4
        
        # Se o número se reduziu a 1, então era uma potência de 3
        return n == 1

# Exemplo de uso
solution = Solution()
param_1 = 64
if solution.isPowerOfFour(param_1):
    print("True")
else:
    print("False")
