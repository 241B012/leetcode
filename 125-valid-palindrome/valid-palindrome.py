class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Filter only alphanumeric characters and convert to lowercase
        filtered = [ch.lower() for ch in s if ch.isalnum()]
        
        # Compare the list with its reverse
        return filtered == filtered[::-1]
