/*
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase alphabet a-z.
*/

#include <string>
#include <iostream>
#include <unordered_map>

using namespace std;

class WordDictionary
{
    class TreeNode
    {
        unordered_map<char, TreeNode *> alphabet;
        bool end;

    public:
        TreeNode()
        {
            end = false;
        };

        TreeNode *get_char(char c)
        {
            return has_char(c) ? alphabet[c] : nullptr;
        }

        bool has_char(char c)
        {
            return alphabet.count(c) == 1;
        }

        void put_char(char c)
        {
            alphabet.insert({c, new TreeNode()});
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

    TreeNode *root;
public:
    /** Initialize your data structure here. */
    WordDictionary()
    {
        root = new TreeNode();
    }

    /** Adds a word into the data structure. */
    void addWord(string word)
    {
        TreeNode *node = root;
        for (auto c:word)
        {
            if (!node->has_char(c))
                node->put_char(c);
            node = node->get_char(c);
        }
        node->set_end();
    }

    bool dfs(TreeNode *node, string target)
    {
        if (node == nullptr)
            return false;
        if (target.empty())
            return node->is_end();
        if (target.front() != '.')
        {
            return dfs(node->get_char(target.front()), target.substr(1, target.size() - 1));
        } else
        {
            for (char c = 'a'; c <= 'z'; ++c)
            {
                if (dfs(node->get_char(c), target.substr(1, target.size() - 1)))
                    return true;
            }
        }
        return false;
    }

    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    bool search(string word)
    {
        return dfs(root, word);
    }
};


int main()
{
    WordDictionary *obj = new WordDictionary();
    obj->addWord("bad");
    obj->addWord("dad");
    obj->addWord("mad");
    cout << obj->search("pad") << endl;
    cout << obj->search("bad") << endl;
    cout << obj->search(".ad") << endl;
    cout << obj->search("b..") << endl;
    return 0;
}
/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */
