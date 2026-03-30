class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = TrieNode()
        ## Creating the Trie for all the words in the dict
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word
        res = []
        def dfs(r,c,node):
            char = board[r][c]

            ## if the char is not in node
            ## children then we skip the path

            if char not in node.children:
                return
            
            ## if char is in node.children
            ## we move to this node and then
            ## we mark it as visited and visit its neighbours
            ## then we backtrack

            node = node.children[char]

            ## If we have reached a leaf(end char of a word)
            if node.word:
                res.append(node.word)
                node.word = None
            
            directions = [(1,0),(0,1),(-1,0),(0,-1)]

            board[r][c] = "#"
            for dr,dc in directions:
                nr,nc = dr+r,dc+c
                if 0<=nr<ROWS and 0<=nc<COLS and board[nr][nc] != "#":
                    dfs(nr,nc,node)
            board[r][c] = char
        
        
        ROWS = len(board)
        COLS = len(board[0])

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root)
        return res