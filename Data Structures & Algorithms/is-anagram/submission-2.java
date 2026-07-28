class Solution {
    public boolean isAnagram(String s, String t) {
        boolean flag = false;
        HashMap<Integer,Character> h1 = new HashMap<>();
        HashMap<Integer,Character> h2 = new HashMap<>();
        for(int i = 0; i < s.length(); i++){
            char k = s.charAt(i);
            h1.put(i,k);
        } // all char in s
        for(int j = 0; j < t.length(); j++){
            char k = t.charAt(j);
            h2.put(j,k);
        } // all char in t
        if(s.length() != t.length()){
            return false;
        }
        else{
            for(Character value: h1.values()){
                if(h2.containsValue(value)){
                    flag = true;
                    h2.values().remove(value);
                }
                else{
                    return false;
                }
            }
        }
        return flag;
        
    }
}
