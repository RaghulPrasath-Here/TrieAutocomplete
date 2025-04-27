package TrieAutocomplete.JavaTrie;
import java.util.ArrayList;
import java.util.Scanner;

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
    public static void dfs(TrieNode node, String word, ArrayList<String> words){
        if(node.isEnd()){
            words.add(word);
        }
        for (int i = 0;i<node.links.length;i++) {
            TrieNode child = node.links[i];
            if(child != null) {
                char ch = (char) ('a' + i);
                dfs(child, word + ch, words);
            }
        }
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Trie trie = new Trie();
        ArrayList<String> words = new ArrayList<>();
        ArrayList<String> output = new ArrayList<>();
        boolean stopAdding = true;
        while(stopAdding){
            System.out.println("Enter word to be added: ");
            words.add(scanner.nextLine());
            System.out.println("Stop Entering? Y or N: ");
            if (scanner.nextLine().toLowerCase().trim().equals("y")){
                stopAdding = false;
            }
        }

        for (String word : words) {
            trie.insert(word);
        }

        boolean stopSearching = true;
        while (stopSearching){
            ArrayList<String> out = new ArrayList<>();
            System.out.println("Enter the string to be searched: ");
            String input = scanner.nextLine();
            TrieNode prefix = trie.startWith(input);
            if(prefix != null){
                dfs(prefix, input, out);
            }
            System.out.println(out);
            System.out.println("Stop Searching? Y or N: ");
            if (scanner.nextLine().toLowerCase().trim().equals("y")){
                stopSearching = false;
            }
        }
    }

}

