# https://leetcode.com/problems/goat-latin/description/
class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        postfix = "maa"
        new_list = []
        for word in S.split():
            if word.startswith(('a','i','e','o','u','A','E','I','O','U')) :
                word=word+postfix
            else:
                word = word[1:]+word[0]+postfix
            postfix = postfix+'a'
            new_list.append(word)
        return " ".join(new_list)

    def toGoatLatin(self, S):
        if not S:
            return S
        aCount = 1
        vowelSet = set(list('aeiouAEIOU'))
        result = []
        for word in S.split():
            if word[0] in vowelSet:
                word = word + 'ma' + 'a'*aCount
            else:
                word = word[1:] + word[0] + 'ma' + 'a'*aCount
            result.append(word)
            aCount += 1
        return ' '.join(result)
    def toGoatLatin(self, S):
        words = S.split()
        vowels = set('aeiouAEIOU')
        ret = []
        for idx, word in enumerate(words, 1):
            if word[0] not in vowels:
                word = word[1:] + word[0]
            word += 'ma'
            word += 'a' * idx
            ret.append(word)
        return ' '.join(ret)