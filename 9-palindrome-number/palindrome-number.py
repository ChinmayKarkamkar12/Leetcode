class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        revnum = 0
        dup = x

        while x > 0:
            ld = x % 10
            revnum = revnum * 10 + ld
            x //= 10

        return dup == revnum