# https://leetcode.com/problems/unique-morse-code-words/description/
class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        concatenation = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        letter = "abcdefghijklmnopqrstuvwxyz"
        mapping = dict(zip(letter,concatenation))
        return len(set("".join([mapping[c] for c in word]) for word in words))