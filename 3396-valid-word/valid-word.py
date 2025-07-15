class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        isVowel = False
        isConsonant = False
        upper = False
        lower = False

        vowels = 'aeiouAEIOU'

        for i in word:
            if not i.isalnum():
                return False
            if i in vowels:
                isVowel = True
            elif i.isalpha():
                isConsonant = True

            if i.isupper():
                upper = True
            if i.islower():
                lower = True

        return isVowel and isConsonant and (upper or lower)
