class Solution {
    public boolean canMakeSubsequence(String str1, String str2) {
        int i = 0;
        int j = 0;
        while(i < str1.length() && j < str2.length()){
            char c1 = str1.charAt(i);
            char c2 = str2.charAt(j);
            int diff = c2-c1;
            if(c1 == c2 || diff == 1 || diff == -25) j += 1;
            i += 1;
        }
        return (j == str2.length())?true:false;
    }
}