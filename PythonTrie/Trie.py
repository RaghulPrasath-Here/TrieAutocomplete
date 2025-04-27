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

    searchedWords = {}

    def dfs(node, string, result):
        if node.isEnd:

            searchedWords[string] = searchedWords.get(string, 0) + 1

            result.append(string)
        
        if len(node.children) == 0:
            return

        for child in node.children.values():
            dfs(child, string + child.value, result)

    # words = ["flower","flow","flight", "clown", "aravind", "athreya", "clock", "aruna"]

    words = []

    with open('words.txt', 'r', encoding='utf-8') as f:
        for line in f:
            word = line.strip()          
            if word:                    
                words.append(word)

    trie = Trie()

    for word in words:
        trie.insert(word)

    while True:
        searchString = input("Enter word to search: ")

        # finding the common node    
        node = trie.startsWith(searchString)
        result = []
        #recursively find all the strings from that common node child
        if node:
            dfs(node, searchString, result)
        
        # sorting the list based on the searchedWords
        result_sorted = sorted(result, key=lambda w: searchedWords.get(w, 0), reverse=True)
        print(result_sorted)
        print(searchedWords)

        end = input("Stop searching? y or n: ").strip().lower()
        if end == "y":
            break