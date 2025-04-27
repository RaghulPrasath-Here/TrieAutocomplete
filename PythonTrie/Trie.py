from collections import defaultdict

class TrieNode:
    def __init__(self, value):
        self.value = value
        self.children = defaultdict()
        self.isEnd = False

    def __str__(self):
        return f"value : {self.value}, children : {list(self.children.keys())}"
    
class Trie:
    def __init__(self):
        self.startNode = TrieNode(" ")

    def insert(self, word: str) -> None:
        currentNode = self.startNode
        for c in word:
            if c in currentNode.children:
                currentNode = currentNode.children[c]
            else:
                node = TrieNode(c)
                currentNode.children[c] = node
                currentNode = node
        
        currentNode.isEnd = True

    def search(self, word: str) -> bool:
        currentNode = self.startNode
        for c in word:
            if c in currentNode.children:
                currentNode = currentNode.children[c]
            else:
                return False

        return currentNode.isEnd

    def startsWith(self, prefix: str) -> object:
        currentNode = self.startNode
        for c in prefix:
            if c in currentNode.children:
                currentNode = currentNode.children[c]
            else:
                return None
        
        return currentNode

if __name__ == "__main__":

    result = []

    def dfs(node, string):
        if node.isEnd:
            result.append(string)
        
        if len(node.children) == 0:
            return

        for child in node.children.values():
            dfs(child, string + child.value)

    words = ["flower","flow","flight", "clown", "aravind", "athreya", "clock", "aruna"]

    trie = Trie()

    for word in words:
        trie.insert(word)

    searchString = input("Enter word : ")

    node = trie.startsWith(searchString)

    if node:
        dfs(node, searchString)
    
    print(result)