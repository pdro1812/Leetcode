class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and (n & (n - 1)) == 0

# Exemplo de uso
solution = Solution()
param_1 = 4
if solution.isPowerOfTwo(param_1):
    print("true")
else:
    print("false")

# O objetivo é descobrir um expoente para 2 que resultasse no numero inputado pelo user
