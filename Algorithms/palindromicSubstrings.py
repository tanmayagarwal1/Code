class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        # dynamic programming table for subset making up to m zeros and n ones
        dp = [ [0 for _ in range(m+1)] for _ in range(n+1)]
        
        # scan each string
        for string in strs:
            
            # total zeros and ones of current string
            zeros = string.count('0')
            ones = len(string) - zeros
            
            # check for each subcase
            for N in range( n, ones-1, -1):
                for M in range( m, zeros-1, -1):
                    
                    # maximize subset size from growing on smaller cases with string
                    dp[N][M] = max( 1 + dp[N-ones][M-zeros], dp[N][M])
                    
        
        return dp[n][m]