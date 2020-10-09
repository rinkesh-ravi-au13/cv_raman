# Question 2:-https://leetcode.com/problems/to-lower-case/


class Solution:
    def toLowerCase(self, str):
        newWord = 'Hello'
        
        for letter in newWord:
            if 65 <= ord(letter) <= 91:
                newWord = chr(ord(letter) + 32)
            else:
                newWord += letter
        return newWord
