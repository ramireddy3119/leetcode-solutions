class Solution {
    public String makeFancyString(String s) {
        int count = 1;
        StringBuffer st = new StringBuffer();
        for(int i = 0; i < s.length();i++){
            if(i > 0){
                if(s.charAt(i-1)==s.charAt(i)){
                    count ++;
                }else{
                    count = 1;
                }
            }
            if(count < 3){
                st.append(s.charAt(i));
            }
        }
        return st.toString();
    }
}