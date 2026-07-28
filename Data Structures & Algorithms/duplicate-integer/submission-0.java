class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> dup = new HashSet<>();
        for(int i = 0; i < nums.length; i++){
            dup.add(nums[i]);
        }
        if(nums.length == dup.size()){
            return false;
        }
        return true;
    }
}