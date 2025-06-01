class Solution {
    public int distributeCandies(int n, int limit) {
        int allCases = ((n+2)*(n+1))/2;  // Total unrestricted ways
        
        if (3 * limit < n) return 0;  // Impossible to distribute
        if (3 * limit == n) return 1; // Only one way when exactly limit for all

        // Compute cases where at least one child gets more than limit candies
        int excludeOne = (n - (limit + 1) + 2);
        int oneLimit = (excludeOne > 1) ? 3 * ((excludeOne * (excludeOne - 1)) / 2) : 0;

        // Compute cases where at least two children get more than limit candies
        int excludeTwo = (n - 2 * (limit + 1) + 2);
        int twoLimit = (excludeTwo > 1) ? 3 * ((excludeTwo * (excludeTwo - 1)) / 2) : 0;

        // Compute cases where all three children get more than limit candies
        int excludeThree = (n - 3 * (limit + 1) + 2);
        int threeLimit = (excludeThree > 1) ? ((excludeThree * (excludeThree - 1)) / 2) : 0;

        // Apply Inclusion-Exclusion Principle
        return allCases - oneLimit + twoLimit - threeLimit;
    }
}
