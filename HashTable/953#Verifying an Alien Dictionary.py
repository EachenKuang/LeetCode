# https://leetcode.com/problems/verifying-an-alien-dictionary/description/
"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order.
The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet,
return true if and only if the given words are sorted lexicographicaly in this alien language.



Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.)
According to lexicographical rules "apple" > "app", because 'l' > '∅',
where '∅' is defined as the blank character which is less than any other character (More info).


Note:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are english lowercase letters.
"""
# 用新的字母顺序表判断所给的数组是否为有序的



class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        d = {v: i  for i, v in enumerate(order)}
        encode_words = []
        # for word in words:
        #     encode_word = ''.join([d[l] for l in word])
        #     encode_words.append(encode_word)
        encode_words = [[d[l] for l in word] for word in words]
        print(encode_words)
        print(sorted(encode_words))
        return sorted(encode_words)==encode_words

if __name__ == '__main__':
    t = Solution()
    print(t.isAlienSorted(["hello","leetcode"],"hlabcdefgijkmnopqrstuvwxyz"))
    print(t.isAlienSorted(["kuvp","n"], "ngxlkthsjuoqcpavbfdermiywz"))