"""
You are given a string s of even length. Split this string into two halves of equal lengths,
 and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels
 ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.

Example 1:

Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.

"""

class Solution:

    def count_vowels (self,half):
        count_val = 0
        for each in half:
            check_vowe = self.check_vowels(each)
            if check_vowe :
                count_val= count_val+1
        return count_val

    def check_vowels(self,s):
        vowel_s = ['a','e','i','o','u']
        if s.lower() in vowel_s:
            return True
        return False

    def halvesAreAlike(self, s: str) -> bool:
        length = len(s)
        first_half = s[:length//2]
        second_half = s[length//2:]
        count_first = self.count_vowels(first_half)
        count_second = self.count_vowels(second_half)
        return count_first == count_second



