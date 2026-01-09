class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        
        def isPalindrome(mask):
            chars = [s[i] for i in range(n) if mask & (1 << i)]
            return chars == chars[::-1]
        
        # Pre-compute palindrome lengths for all masks
        pal_len = {}
        for mask in range(1, 1 << n):
            if isPalindrome(mask):
                pal_len[mask] = bin(mask).count('1')
        
        max_product = 0
        masks = list(pal_len.keys())
        
        for i, m1 in enumerate(masks):
            for m2 in masks[i+1:]:
                if m1 & m2 == 0:  # Disjoint
                    max_product = max(max_product, pal_len[m1] * pal_len[m2])
        
        return max_product