package TrieAutocomplete.JavaTrie;
public class TrieNode {
    TrieNode[] links = new TrieNode[26];
    boolean flag = false;

    public TrieNode() {
    }

    boolean containsKey(char ch) {
        return links[ch - 'a'] != null;
    }

    TrieNode get(char ch) {
        return links[ch - 'a'];
    }

    void put(TrieNode node, char ch) {
        links[ch - 'a'] = node;
    }

    boolean isEnd() {
        return flag;
    }

    void setEnd() {
        flag = true;
    }

}
