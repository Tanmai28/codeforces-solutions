**Prime Square**


To construct a prime square of size n × n, we need to satisfy three conditions:

**✅ Prime Square Conditions:**

        All numbers are non-negative integers ≤ 10⁵
        
        No number in the square is prime
        
        Each row and column sum must be a prime number


**🔨 Construction Strategy**

Let’s fix all cells to 1 (non-prime). The row sum would be n × 1 = n.

But n may not be prime, so we’ll:

      Use 1 in most cells
      
      Replace one cell per row with a number so the row sum becomes a prime
      
      Ensure all such tweaks are non-prime numbers


**✅ Algorithm Steps:**

For each test case:

      Find a prime number p > n such that p - (n - 1) is non-prime
      
      Fill the row with n-1 ones and one p - (n - 1) (completes the row sum to prime p)
      
      Rotate the row per row (to spread out the bigger value and balance columns)

