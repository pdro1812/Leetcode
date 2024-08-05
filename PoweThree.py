class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        
        # Divide n por 3 até que não seja mais divisível
        while n % 3 == 0:
            n //= 3   
            
        return n == 1

# Exemplo de uso
solution = Solution()
param_1 = 27
if solution.isPowerOfThree(param_1):
    print("True")
else:
    print("False")
