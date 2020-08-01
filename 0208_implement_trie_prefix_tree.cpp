/*
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
*/


#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

class Trie
{
    // search tree

    class TrieNode
    {
        unordered_map<char, TrieNode *> char_map;
        bool end{};
    public:
        TrieNode() = default;

        TrieNode *get_next(char c)
        {
            return char_map[c];
        }

        void put_char(char c)
        {
            char_map[c] = new TrieNode();
        }

        bool has_char(char c)
        {
            return char_map.count(c);
        }

        void set_end()
        {
            end = true;
        }

        bool is_end()
        {
            return end;
        }
    };

    TrieNode *root;

public:
    /** Initialize your data structure here. */
    Trie()
    {
        root = new TrieNode();
    }

    /** Inserts a word into the trie. */
    void insert(string word)
    {
        TrieNode *node = root;
        for (char c: word)
        {
            if (!node->has_char(c))
                node->put_char(c);
            node = node->get_next(c);
        }
        node->set_end();
    }

    /** Returns if the word is in the trie. */
    bool search(string word)
    {
        TrieNode *node = root;
        for (char c:word)
        {
            if (!node->has_char(c))
                return false;
            node = node->get_next(c);
        }
        return node->is_end();
    }

    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix)
    {
        TrieNode *node = root;
        for (char c:prefix)
        {
            if (!node->has_char(c))
                return false;
            node = node->get_next(c);
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
