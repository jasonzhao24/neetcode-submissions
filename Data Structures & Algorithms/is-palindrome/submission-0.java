class Solution {
    public boolean isPalindrome(String s) {
        String cleanStr = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        int beginning = 0;
        int end = cleanStr.length()-1;
        while(beginning < end){
            if(!cleanStr.substring(beginning,beginning+1).equals(cleanStr.substring(end,end+1))){
                return false;
            }
            beginning++;
            end--;
        }
        return true;
    }
}
