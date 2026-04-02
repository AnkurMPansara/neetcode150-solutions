class TrieNode():
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
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)
        ROWS, COLS = len(board), len(board[0])
        res = set()
        visit = set()
        
        def backtracking(r, c, node, word):
            if r<0 or c<0 or r==ROWS or c==COLS or ((r,c) in visit) or (board[r][c] not in node.child):
                return
            visit.add((r,c))
            node = node.child[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
            backtracking(r+1, c, node, word)
            backtracking(r-1, c, node, word)
            backtracking(r, c+1, node, word)
            backtracking(r, c-1, node, word)
            visit.remove((r,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                backtracking(r, c, root, "")
        
        return list(res)
        