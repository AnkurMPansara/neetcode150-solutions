class Solution {
    public int minDistance(String word1, String word2) {
        int n = word1.length();
        int m = word2.length();
        int[][] dp = new int[n+1][m+1];

        for(int i=n;i>=0;--i) {
            for(int j=m;j>=0;--j) {
                if(i==n && j==m) {
                    dp[i][j] = 0;
                    continue;
                }
                if(i==n && j!=m) {
                    dp[i][j] = m-j;
                    continue;
                }
                if(i!=n && j==m) {
                    dp[i][j] = n-i;
                    continue;
                }
                if(word1.charAt(i) == word2.charAt(j)) {
                    dp[i][j] = dp[i+1][j+1];
                } else {
                    dp[i][j] = 1 + Math.min(dp[i+1][j], Math.min(dp[i][j+1], dp[i+1][j+1]));
                }
            }
        }

        return dp[0][0];
    }
}
