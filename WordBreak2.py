# Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

# Return all such possible sentences.

# For example, given
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].

# A solution is ["cats and dog", "cat sand dog"].

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        breakable = []
        breakable0 = [False] * len(s)
        for i in range(len(s)):
            for w in dict:
                if w == s[i - len(w) + 1 : i + 1] and ( breakable0[i - len(w)] or i - len(w) == -1):
                    breakable0[i] = True
        if breakable0[-1] == False:
            return []
        for i in range(len(s)):
            breakable.append([])
            for w in dict:
                if w == s[i - len(w) + 1 : i + 1]:
                    if i - len(w) == -1:
                        breakable[i].append(w)
                    elif len( breakable[i - len(w)]) > 0:
                        for so in breakable[i - len(w)]:
                            breakable[i].append(so + " " + w)
        return breakable[-1]

if __name__ == '__main__' :
    # s = "catsanddog"
    # dict = ["cat", "cats", "and", "sand", "dog"]
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    dict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    # s = "abcd"
    # dict = ["a", "abc", "b", "cd", "dog"]
    # s = "aaaaaaa"
    # dict = ["aaaa", "aaa", "b", "cd", "dog"]
    print Solution().wordBreak( s, dict)
