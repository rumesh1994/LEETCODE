class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Split the words in a sentence, reverse each word and join them using a space to form a sentence
        # string.split(s[, sep[, maxsplit]]); string.join(words[, sep])
        return ' '.join([word[::-1] for word in s.split(' ')])