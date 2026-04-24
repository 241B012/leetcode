from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        n = len(words)
        
        while i < n:
            # Step 1: take words for current line
            line_words = []
            line_len = 0
            
            while i < n and line_len + len(words[i]) + len(line_words) <= maxWidth:
                line_words.append(words[i])
                line_len += len(words[i])
                i += 1
            
            gaps = len(line_words) - 1
            line = ""
            
            # Step 2: last line OR single word → left justify
            if i == n or gaps == 0:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            
            else:
                spaces = maxWidth - line_len
                each_gap = spaces // gaps
                extra = spaces % gaps
                
                for j in range(gaps):
                    line += line_words[j]
                    line += " " * (each_gap + (1 if j < extra else 0))
                
                line += line_words[-1]
            
            res.append(line)
        
        return res