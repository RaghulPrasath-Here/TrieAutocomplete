package TrieAutocomplete.JavaTrie;

public class Trie {
    private static TrieNode root;

    Trie(){
        root = new TrieNode();
    }
    public void insert(String word){
        TrieNode node = root;

        for (int i = 0;i<word.length();i++){
            char ch = word.charAt(i);
            if(!node.containsKey(ch)){
                node.put(new TrieNode(), ch);
            }
            node = node.get(ch);
        }
        node.setEnd();
    }

    public boolean search(String word){
        TrieNode node = root;
        for (int i = 0; i<word.length();i++){
            char ch = word.charAt(i);
            if(!node.containsKey(ch)){
                return false;
            }
            node = node.get(ch);
        }
        if(node.isEnd()){
            return true;
        }
        return false;
    }

    public TrieNode startWith(String word){
        TrieNode node = root;
        for (int i = 0; i<word.length();i++){
            char ch = word.charAt(i);
            if(!node.containsKey(ch)){
                return null;
            }
            node = node.get(ch);
        }
        return node;
    }
}
