package Lab07.pack;
import java.util.Arrays;
import java.lang.Math;

public class EqualsSubsets {
    public boolean canPartition_Recurse(int[] arr) {
        int sum = 0;
        for (int i : arr) {
            sum += i;
        }
        if (sum % 2 != 0)  return false;
        return recurse(arr, 0, sum / 2);
    }
    
    public boolean canPartition_Memoiz(int[] arr) {
        int target = 0;
        for (int i = 0; i < arr.length; i++) {
            target += arr[i];
        }
        if (target % 2 != 0) {
            return false; 
        }
        target /= 2;
        return memoiz(arr, target, 0, new Boolean[arr.length][target + 1]);
    }

    public boolean canPartition_DP(int[] arr) {
        // return false;
        return dp(arr);
    }

    private boolean recurse(int[] arr, int idx, int sum) {
        if (sum < 0) return false;
        if (sum == 0) return true;
        if (idx < arr.length - 1) {
            return recurse(arr, idx + 1, sum - arr[idx]) || recurse(arr, idx + 1, sum);
        }
        return sum - arr[idx] == 0;
    }

    private boolean memoiz(int[] arr, int target, int index, Boolean[][] cache) {
        if (target == 0) {
            return true;
        }
        if (target < 0 || index >= arr.length) {
            return false;
        }
        if (cache[index][target] != null) {
            return cache[index][target];
        }
        boolean include = memoiz(arr, target - arr[index], index + 1, cache);
        boolean exclude = memoiz(arr, target, index + 1, cache);
        cache[index][target] = include || exclude;
        return cache[index][target];
    }

    private boolean dp(int[] arr) {
        int n = arr.length;
        int sum = 0;
        for (int i = 0; i < arr.length; i++) {
            sum += arr[i];
        }
        if (sum % 2 != 0) {
            return false;
        }

        sum /= 2;

        boolean[][] dp = new boolean[n + 1][sum + 1];
        for (int i = 0; i <= n; i++) {
            dp[i][0] = true;
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= sum; j++) {
                if (j < arr[i - 1]) {
                    dp[i][j] = dp[i - 1][j];
                } else {
                    dp[i][j] = dp[i - 1][j] || dp[i - 1][j - arr[i - 1]];
                }
            }
        }

        return dp[n][sum];
    }
}
