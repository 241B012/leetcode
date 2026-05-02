class Solution:
    def rotatedDigits(self, n: int) -> int:
        valid = {0, 1, 2, 5, 6, 8, 9}
        change = {2, 5, 6, 9}
        
        count = 0
        
        for num in range(1, n + 1):
            x = num
            is_valid = True
            has_changed = False
            
            while x > 0:
                d = x % 10
                
                if d not in valid:
                    is_valid = False
                    break
                if d in change:
                    has_changed = True
                
                x //= 10
            
            if is_valid and has_changed:
                count += 1
        
        return count