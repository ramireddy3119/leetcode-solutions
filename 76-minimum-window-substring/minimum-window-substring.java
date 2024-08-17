import java.util.HashMap;

class Solution {
    public String minWindow(String s, String t) {
        if (s == null || t == null || s.length() < t.length()) {
            return "";
        }

        HashMap<Character, Integer> hash = new HashMap<>();
        for (char c : t.toCharArray()) {
            hash.put(c, hash.getOrDefault(c, 0) + 1);
        }

        int l = 0, r = 0;
        int minlen = Integer.MAX_VALUE;
        int index = -1;
        int count = 0; 

        while (r < s.length()) {
            char rightChar = s.charAt(r);
            if (hash.containsKey(rightChar)) {
                hash.put(rightChar, hash.get(rightChar) - 1);
                if (hash.get(rightChar) >= 0) {
                    count++;
                }
            }

            while (count == t.length()) {
                if (r - l + 1 < minlen) {
                    minlen = r - l + 1;
                    index = l;
                }

                char leftChar = s.charAt(l);
                if (hash.containsKey(leftChar)) {
                    hash.put(leftChar, hash.get(leftChar) + 1);
                    if (hash.get(leftChar) > 0) {
                        count--;
                    }
                }
                l++;
            }
            r++;
        }

        return index == -1 ? "" : s.substring(index, index + minlen);
    }
}
