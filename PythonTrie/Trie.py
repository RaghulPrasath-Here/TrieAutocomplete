from collections import defaultdict

class TrieNode:
    def __init__(self, value):
        self.value = value
        self.children = {}
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

    def dfs(node, string, result):
        if node.isEnd:
            result.append(string)
                  
        if len(node.children) == 0:
            return

        for child in node.children.values():
            dfs(child, string + child.value, result)

    def sort_chars_lex(s: str) -> str:
        return "".join(sorted(s))

    def is_subsequence(small: str, large: str) -> bool:
        it = iter(large)
        return all(ch in it for ch in small)

    words = []
    searchedWords = {}

    #reading the words from the words.txt and storing it in words list
    with open('words.txt', 'r', encoding='utf-8') as f:
        for line in f:
            word = line.strip()          
            if word:                    
                words.append(word)

    # initializing trie 
    trie = Trie()

    #inserting the words into the trie
    for word in words:
        trie.insert(word)
    
    while True:
        # to collect the similar words if the searchedString is not present in the words
        similarWords = []
        currentWordsCount = {}

        searchString = input("Enter a word to see all the words that starts with it : ")

        if searchString not in words:
            sortedSearchString = sort_chars_lex(searchString)
            # add words with same starting character as of inputString to a list
            for word in words:
                if word[0] == searchString[0]:
                    sortedWord = sort_chars_lex(word)
                    #checking whether the searchedString is a subsequence of the words
                    if is_subsequence(sortedSearchString, sortedWord):
                        similarWords.append(word)

            if len(similarWords) > 0:
                similarWords_sorted = sorted(similarWords, key=lambda w: searchedWords.get(w, 0), reverse=True)
                choosedWord = ""
                while choosedWord not in similarWords:
                    print("Did you mean?")
                    print(similarWords_sorted)
                    print("\nChoose a word from the above list you want to search (1 for the 1st word)")
                    similarChoice = int(input())
                    if similarChoice > len(similarWords):
                        continue
                    
                    choosedWord = similarWords_sorted[similarChoice-1]
                    node = trie.startsWith(choosedWord)
                    result = []
                    if node:
                        dfs(node, choosedWord, result)

                    for word in result:
                        if word not in searchedWords:
                            currentWordsCount[word] = 0
                        else:
                            currentWordsCount[word] = searchedWords[word]
                    index = None
                    for i, (s, count) in enumerate(currentWordsCount.items()):
                        if s == choosedWord:
                            index = i
                            break 
                    searchedWords[choosedWord] = currentWordsCount.get(choosedWord, 0) + 1
                    print(searchedWords)
                
            else:
                print("Enter a valid word... ")
                continue
        
        else:
            node = trie.startsWith(searchString)
            result = []
            
            #recursively find all the strings from that common node child
            if node:
                dfs(node, searchString, result)

            for word in result:
                if word not in searchedWords:
                    currentWordsCount[word] = 0
                else:
                    currentWordsCount[word] = searchedWords[word]

            currentWordsCount = sorted(currentWordsCount.items(), key=lambda item: item[1], reverse=True)
            currentWordsCount = currentWordsCount[0:10]
            if(len(result) == 1):
                index = None
                for i, (s, count) in enumerate(currentWordsCount):
                    if s == searchString:
                        index = i
                        break
                searchedWords[searchString] = currentWordsCount[index][1]+1
                print(searchedWords)
                continue

            else:
                result_sorted = sorted(result, key=lambda w: searchedWords.get(w, 0), reverse=True)
                print(f"\nWords that start with {searchString}")
                print("\nChoose a word from the below list you want to search (1 for the 1st word)")
                print(result_sorted)
                
                choice = int(input())
                index = None
                for i, (s, count) in enumerate(currentWordsCount):
                    if s == result_sorted[choice - 1]:
                        index = i
                        break
                searchedWords[result_sorted[choice - 1]] = currentWordsCount[index][1]+1

                print(f"Searched Words count {searchedWords}")

        end = input("Stop searching? y or n: ").strip().lower()
        if end == "y":
            break
