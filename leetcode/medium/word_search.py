class Solution:
    def __init__(self):
        self.n = 0
        self.m = 0

    def exist(self, board, word) -> bool:
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.n = len(board)
        self.m = len(board[0])
        for i in range(self.n):
            for j in range(self.m):
                if word[0] == board[i][j]:
                    if self.backtrack(board,word,i,j,0,""):
                        return True
        return False
        
    def backtrack(self, board, word, i, j, indx, w) -> bool:
        if i < 0 or i >= self.n or j < 0 or j >= self.m: return False
        if board[i][j] != word[indx]: return False              
        if board[i][j] == "*": return False

        w += board[i][j]
        if w == word: return True

        temp = board[i][j]
        board[i][j] = "*"
        indx +=1

        find = self.backtrack(board, word, i+1, j, indx, w) or \
            self.backtrack(board, word, i-1, j, indx, w) or \
            self.backtrack(board, word, i, j+1, indx, w) or \
            self.backtrack(board, word, i, j-1, indx, w) 

        board[i][j] = temp
        indx -= 1
        
        return find