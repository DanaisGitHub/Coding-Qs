
# come back to this one

class Solution:
    
    def rowAndColChecker(self,board:List[List[str]],x:int,y:int)->bool:
        rowLength = len(board)
        colLength = len(board[0])
        char = board[x][y]
        
        for i in range(9):
            if char == board[i][y] or char == board[x][i]:
                return True
        
        return False
            
    
    
    
    
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        xyLimit1,xyLimit2 = 2,2
        
        while xyLimit1<=9: 
        
            for i in range(xyLimit1-2,xyLimit1):
                
                while xyLimit2<=9:
                    
                    threeBy3Map = {}
                    
                    for j in range(xyLimit2-2,xyLimit2):
                        if board[i][j] == ".":
                            continue
                        threeBy3Map[board[i][j]] = 1+threeBy3Map[board[i][j]] if board[i][j] in threeBy3Map else 0 # or is it 1
                        if threeBy3Map[board[i][j]] > 1:
                            return False
                        if self.rowAndColChecker(board,i,j):
                            return False
                    xyLimit2+=3
            xyLimit1+=3
            
            
            
            
            

        
                