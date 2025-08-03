**UpScalling**


🧠** Key Observations**

        Each 2×2 block is filled with either:     #  or   .
        
        The pattern alternates, like a chessboard — but in 2×2 chunks.
        
        The top-left 2×2 block is #.

        
<img width="965" height="392" alt="image" src="https://github.com/user-attachments/assets/7f7ca46c-158f-4348-8f65-d265c7ed5085" />


✅ Pattern Insight
        For a given n, we are to generate a 2n × 2n grid.
        
        We fill it using nested loops:
        
        Every 2 rows form a block row
        
        Every 2 columns form a block column
        
        The block at (i // 2, j // 2) determines if we print # or . :

              If (i // 2 + j // 2) % 2 == 0: use #
              
              Else: use .
