    def addDigits(self, num: int) -> int:
        while num >= 10:  
            num = sum(int(i) for i in str(num))  
        return num

solution = Solution()
result = solution.addDigits(38)
print(result)  
