class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfDigitSquared(n: int) -> int:
            res = 0
            while n > 0:
                res += (n%10)**2
                n = n//10
            return res
        
        fast, slow = n, n
        while True:
            slow = sumOfDigitSquared(slow)
            fast = sumOfDigitSquared(sumOfDigitSquared(fast))
            if fast == 1:
                return True
            if slow == fast:
                return False