class Solution {
    public int countConsistentStrings(String allowed, String[] words) {
        int count = words.length;

        for (String word : words) {
            for (int j = 0; j < word.length(); j++) {
                if (allowed.indexOf(word.charAt(j)) == -1) { // check if char is not in allowed
                    count--;
                    break;
                }
            }
        }

        return count;
    }
}
