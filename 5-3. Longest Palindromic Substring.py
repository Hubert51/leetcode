## 注意写helper function
## 改动member variable 记得检查所有有关的变量

class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.longestNum = 0
        self.result = ""
        self.length = len(s)
        self.s = s
        
        # base case:
        if len(s) == 0:
            return ""
        elif len(s) == 1:
            return s
        elif len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        else:
            self.longestNum = 1
            self.result = s[0]
        
        for index in range(len(s)):
            # base case
            if index == 0 and s[0] == s[1]:
                longestNum = 2
                result = s[0:2]

            # ABA mode:
            self.helper(index-1, index+1)

            # ABBA mode:
            self.helper(index-1, index)
        return self.result

                
    def helper(self, front, back):
        while front >= 0 and back < self.length:
            if  self.s[front] ==  self.s[back]:
                if back+1 - front > self.longestNum:
                    self.longestNum = back+1-front
                    self.result = self.s[front:back+1]
                front -= 1
                back += 1
                
            else:
                break
                
