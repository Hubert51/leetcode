class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        score = 0
        
        startIndex = 0
        endIndex = len(height)
        index = startIndex
        leftBound = False
        leftHeight = 0
        while True:
            # two situations here. IMPORTMENT! 我忘记了第二种情况
            # [4,2,3]
            # [3,2,1,3,1]
            if index == len(height):
                # minus 2 is importment here
                if startIndex >= len(height)-2:
                    break
                elif height[startIndex] > height[startIndex+1]:
                    height[startIndex] -= 1
                    leftHeight -= 1
                else:
                    startIndex += 1
                index = startIndex
                leftBound = False
                
            if leftBound == False:
                if index >= len(height):
                    break
                if height[index] == 0:
                    index += 1
                    startIndex += 1
                    continue
                    
                else:
                    leftBound = True
                    leftHeight = height[index]
                    index += 1
            
            else:
                if height[index] < leftHeight:
                    index += 1
                    continue
                
                else:
                    endIndex = index
                    for element in height[startIndex+1:endIndex]:
                        score += leftHeight - element
                    startIndex = index
                    leftBound = False
        return score
                    
