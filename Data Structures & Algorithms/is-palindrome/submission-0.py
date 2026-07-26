
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean =[]
        for ch in s:
            if ch.isalnum():
                clean.append(ch.lower())
        clean_text = ''.join(clean)
        return clean_text == clean_text[::-1]

        