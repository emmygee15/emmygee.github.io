#find the maximum score that a player can get 
import math 
  
def minimax (curDepth, nodeIndex, maxTurn, scores, targetDepth): 
    print("curDepth, nodeIndex ", curDepth, nodeIndex)
    print("maxTurn",maxTurn)
    # base case : targetDepth reached 
    if (curDepth == targetDepth):  
        print("Exiting because curDepth = targetDepth with  scores[nodeIndex] ", scores[nodeIndex] )
        return scores[nodeIndex] 
      
    if (maxTurn): 
        print("in Max")
        left=minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth)
        right=minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth)
        print("left & right have",left,right)
        p=max(left,right) 
        print("Max returning ",p)
        
        return p
      
    else: 
        print("in Min")
        left=minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth)
        right=minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth)
        print("left & right have",left,right)
        p=min(left,right) 
        print("Min returning ",p)
        return p
      
# Driver code 
scores = [5, 6, 4, 7, 7, 6, 1, -9, 1, 0, 0, -4, 4, -1, 2, -3] 
  
treeDepth = math.log(len(scores), 2) 
  
#start with Max player maxTurn=True
print("The optimal value is : ",minimax(0, 0, True, scores, treeDepth)) 
  

