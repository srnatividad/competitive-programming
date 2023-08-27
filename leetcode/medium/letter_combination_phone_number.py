class Solution(object):
    def __init__(self):
        self.temp = []
        self.stack = []
        self.numbers = ['','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        
    def combination(self,nums, l, offset, n):
        if n == 0:
            self.stack.append("".join(self.temp))
        else:
            for i in range(offset, l-n+1):
                for j in nums[i]:
                    self.temp.append(j)
                    self.combination(nums, l, i+1, n-1)
                    self.temp.pop()

                    
    def letterCombinations(self, digits):
        if digits == "": return []
        
        nums = []
        for i in list(digits):
            nums.append(self.numbers[int(i)-1])
        
        if len(nums) == 1: 
            return list(nums[0])
        
        self.combination(nums, len(nums), 0, len(nums))
        return self.stack