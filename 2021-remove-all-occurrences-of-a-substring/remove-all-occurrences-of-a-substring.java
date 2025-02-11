class Solution {
    public String removeOccurrences(String s, String target) {
        StringBuilder sb = new StringBuilder();
        for (char ch : s.toCharArray()) {
            sb.append(ch);
            if (sb.length() >= target.length() && 
                sb.substring(sb.length() - target.length()).equals(target)) {
                sb.delete(sb.length() - target.length(), sb.length());
            }
        }
        return sb.toString();
    }


}