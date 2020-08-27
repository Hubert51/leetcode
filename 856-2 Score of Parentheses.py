class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        score = 0
        if len(S) == 0:
            return 0
        if len(S) == 2:
            return 1
        
        balance = 0
        index = 0
        while True:
            if S[index] == "(":
                balance += 1
            elif S[index] == ")":
                balance -= 1
            
            if balance == 0:
                subString = S[1:index]
                if len(subString) == 0:
                    score += 1
                else:
                    score += 2 * self.scoreOfParentheses(S[1:index])
                if index == len(S)-1:
                    break
                else:
                    S = S[index+1:]
                    index = 0
                    continue
            index += 1
                
        return score
        
        
        