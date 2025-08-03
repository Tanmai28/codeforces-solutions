_**Thorns and Coins**_



**🧠 Problem Summary**

You're given a path of n cells. Each cell can be:
      
      . → empty
      
      @ → coin
      
      * → thorns (blocked)

You start at position 0, which is always empty.
From any position i, you can move to:

    i + 1 (if not thorns and within bounds)
    
    i + 2 (if not thorns and within bounds)

Your goal is to collect the maximum number of coins by making legal moves.



<img width="1023" height="157" alt="image" src="https://github.com/user-attachments/assets/796514d2-4aca-477c-95b9-9a0b9bd3111c" />


**✅ DP Approach**

Let dp[i] be the maximum number of coins collected starting from position i.

We build dp[i] from right to left:

      dp[i] = max(dp[i+1], dp[i+2]) + (1 if path[i] == '@' else 0)
      
But we must ensure:

      i+1 and i+2 are within bounds
      
      path[i+1] or path[i+2] is not *
      
      Can't step into *
