class Solution:
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1: #  the last bit of odd numbers is always 1 while it's always 0 for even numbers. so if n&1 is true, n is an odd number.
                pow *= x
            x *= x
            n >>= 1
        return pow


