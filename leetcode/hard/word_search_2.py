class TrieNode:
    def __init__(self):
        self.child = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.child:
                cur.child[c] = TrieNode()
            cur = cur.child[c]
        cur.isWord = True

class Solution:
    def __init__(self):
        self.row = 0
        self.col = 0
        self.res = set()
        self.vis = set()
    
    def dfs(self, board, node, r, c, word):
        if (r < 0 or r == self.row or c < 0 or c == self.col) or \
            ((r, c) in self.vis) or (board[r][c] not in node.child):
            return
        
        self.vis.add((r,c))
        node = node.child[board[r][c]]
        word += board[r][c]
        if node.isWord:
            self.res.add(word)

        self.dfs(board, node, r+1, c, word)
        self.dfs(board, node, r-1, c, word)
        self.dfs(board, node, r, c+1, word)
        self.dfs(board, node, r, c-1, word)

        self.vis.remove((r,c))

    def findWords(self, board, words):
        root = TrieNode()
        for w in words:
            root.addWord(w)

        self.row, self.col = len(board), len(board[0])

        for r in range(self.row):
            for c in range(self.col):
                self.dfs(board, root, r, c, "")
        
        return list(self.res)