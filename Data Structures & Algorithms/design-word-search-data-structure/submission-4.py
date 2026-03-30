class TrieNode:
    def __init__(self):
        self.children = {}
        self.flag = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.flag = True

    def search(self, word: str) -> bool:
        def dfs(node,idx):
            if idx == len(word):
                return node.flag
            
            ch = word[idx]

            if ch == ".":
                for child in node.children.values():
                    if dfs(child,idx+1):
                        return True
                return False
            else:
                if ch not in node.children:
                    return False
                return dfs(node.children[ch],idx+1)
        return dfs(self.root,0)

