# 很粗心，题目都没看清，这里不仅要数量匹配，还要order匹配。
# 有个corner case 没考虑清楚。如果先出现后面那个，所以要加13行代码
class Solution:
    def isValid(self, s: str) -> bool:
        a = 0
        b = 0
        c = 0
        charQuene = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                charQuene.append(char)
            else:
                if len(charQuene) == 0:
                    return False
                if charQuene[-1]=="(" and char==")" or charQuene[-1]=="[" and char=="]" or charQuene[-1]=="{" and char=="}":
                    charQuene.pop()
                else:
                    return False
        return len(charQuene)==0
            
        
