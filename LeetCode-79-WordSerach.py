from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(x:int, y:int, suffix:str) -> bool:
            if len(suffix) == 0:
                return True
            
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y]!=suffix[0]:
                return False
        
        
            temp = board[x][y]
            board[x][y]=''
            result = dfs(x+1, y, suffix[1:]) or dfs(x, y+1,  suffix[1:]) or dfs(x-1, y, suffix[1:]) or dfs(x,y-1,suffix[1:])
            board[x][y]=temp
            return result
    
        for i in range(len(board)):
            for j in range(len(board[i])):
                if dfs(i,j,word):
                    return True
        return False

x = Solution()
#print(x.exist([["a","b"],["c","d"]],"bacd"))
print(x.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"))


