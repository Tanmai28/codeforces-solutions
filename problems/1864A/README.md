🧩**Problem Summary**

You have n ropes, each tied to a nail on a wall at height aᵢ.
Each rope is of length bᵢ.
All the other ends of these ropes are tied together to one single candy.

You can imagine the candy as being pulled up by all ropes at once, so it's suspended at the highest point any rope allows it to go.

🎯 **Goal**

You want to bring the candy down to the ground (height 0) by cutting as few ropes as possible.

🧠 **Understanding How the Candy Hangs**

For each rope:

         Nail is at height aᵢ. 
         Rope length is bᵢ. 
         So the rope can reach as low as aᵢ - bᵢ. 
         But since all ropes are tied to the candy, the candy can't go lower than the highest of these aᵢ - bᵢ values.
 
Why? Because the shortest effective rope pulls the candy up, limiting how low it can hang.

**Find the minimum number of ropes to cut so that the maximum of aᵢ - bᵢ among remaining ropes ≤ 0.**


🔁 **Strategy**

          Compute aᵢ - bᵢ for each rope.
          
          This represents the lowest point that each rope allows.
          
          The maximum of these values determines how high the candy hangs.
          
          To lower the candy, cut ropes in descending order of aᵢ - bᵢ (start with ropes that keep the candy highest).
          
          Keep cutting until the new max ≤ 0.

**Example:**

        Input:
          4 ropes:
          (9, 2) → aᵢ - bᵢ = 7
          (5, 2) → aᵢ - bᵢ = 3
          (7, 7) → aᵢ - bᵢ = 0
          (3, 4) → aᵢ - bᵢ = -1
          
          → hang_heights = [7, 3, 0, -1]
          
          → initial candy height = max = 7
          → cut rope with 7 → hang_heights = [3, 0, -1]
          → new max = 3 → cut again
          → hang_heights = [0, -1]
          → new max = 0 → candy reaches ground ✅
          
        Result: **2 cuts**
